from functools import partial

from .parser import Parser
from .reports import BaseReporter
from .utils import get_file_data_by_path, reporters, filter_by_date


class Processor:
    def __init__(self) -> None:
        args: Parser = Parser().parse_args()
        data = []
        for logfile in args.file:
            data.extend(get_file_data_by_path(logfile))
        if not data:
            return print("Nothing to report")
        reporter: BaseReporter = reporters.get(args.report)
        if not reporter:
            return print("Invalid report type")
        if args.date is not None:
            data = tuple(filter(partial(filter_by_date, args.date), data))
        reporter(data)
