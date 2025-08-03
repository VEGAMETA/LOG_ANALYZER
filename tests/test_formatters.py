from app.formatters.tabulate import TabulateFormatter
from app.formatters.base import BaseFormatter
import pytest


def test_base_formatter_abstract_method():
    with pytest.raises(TypeError):
        BaseFormatter()


def test_tabulate_formatter(capsys):
    data = [("item1", 1, 0.1), ("item2", 2, 0.2)]
    headers = ["Name", "Count", "Time"]
    TabulateFormatter.format(data, headers)
    captured = capsys.readouterr()
    assert "item1" in captured.out
    assert "item2" in captured.out
    assert "Name" in captured.out
    assert "Count" in captured.out
    assert "Time" in captured.out
