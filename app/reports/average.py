from .base import BaseReporter


class ReporterAverage(BaseReporter):
    report_type = "average"

    def report(self) -> None:
        self.out = {}
        self.headers = ["handler", "total", "avg. reponse time"]
        for chunk in self.data:
            handler = chunk.get("url")
            if not handler:
                continue
            time = chunk.get("response_time", None)
            if time is None:
                continue
            try:
                self.out[handler]["total"] += 1
                self.out[handler]["time"] += time
            except KeyError:
                self.out[handler] = {"total": 1, "time": time}
        self.out = [
            (
                handler,
                self.out[handler]["total"],
                "%.3f" % (self.out[handler]["time"] / self.out[handler]["total"]),
            )
            for handler in self.out.keys()
        ]
        if not self.out:
            return
        self.out = sorted(self.out, key=lambda x: x[1], reverse=True)
