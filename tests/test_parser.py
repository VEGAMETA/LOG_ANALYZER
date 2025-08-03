from app.parser import Parser
from datetime import date
import pytest


def test_parser_with_required_args():
    parser = Parser()
    args = parser.parse_args(["-f", "file1.log", "file2.log", "-r", "average"])
    assert args.file == ["file1.log", "file2.log"]
    assert args.report == "average"
    assert args.date is None


def test_parser_with_date():
    parser = Parser()
    args = parser.parse_args(["-f", "file1.log", "-r", "average", "-d", "2025-25-05"])
    assert args.date == date(2025, 5, 25)


def test_parser_missing_required_args():
    parser = Parser()
    with pytest.raises(SystemExit):
        parser.parse_args([])
