from tabulate import tabulate

from .base import BaseFormatter


class TabulateFormatter(BaseFormatter):
    @classmethod
    def format(cls, data: list, headers: list) -> None:
        print(tabulate(data, headers, "rounded_outline", showindex="always"))
