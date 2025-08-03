from abc import ABC, abstractmethod

from .. import formatters


class BaseReporter(ABC):
    def __init__(
        self,
        data: list | dict | tuple = [],
        /,
        formatter: formatters.BaseFormatter = formatters.TabulateFormatter,
        **kwargs,
    ) -> None:
        self.data: list = data
        self.out: list | dict | tuple = {}
        self.headers = []
        self.report()
        if not self.out:
            return
        formatter.format(data=self.out, headers=self.headers)

    @abstractmethod
    def report(self) -> None: ...
