import argparse

from datetime import datetime

from .utils import reporters


class Parser(argparse.ArgumentParser):
    def __init__(self) -> None:
        super().__init__()
        self.formatter_class = argparse.RawDescriptionHelpFormatter
        self.description = "Simple logs processing script\n"
        self.description += "\nREPORT TYPES:"
        for report_type in reporters.keys():
            self.description += f"\n\t{report_type}"
        self.add_argument(
            "-f",
            "--file",
            nargs="+",
            type=str,
            required=True,
            help="provide path to log file(s)",
        )
        self.add_argument(
            "-r",
            "--report",
            type=str,
            required=True,
            help="provide report type",
        )
        self.add_argument(
            "-d",
            "--date",
            type=lambda s: datetime.strptime(s, "%Y-%d-%m").date(),
            help="[optional] date in YYYY-DD-MM format",
        )
