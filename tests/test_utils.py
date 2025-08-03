import pytest
from functools import partial
from app.utils import get_file_data_by_path, filter_by_date
from datetime import date


def test_get_file_data_by_path_valid_file(log_file, sample_log_data):
    result = get_file_data_by_path(log_file)
    assert len(result) == len(sample_log_data)
    assert result == sample_log_data


def test_get_file_data_by_path_empty_file(empty_log_file):
    result = get_file_data_by_path(empty_log_file)
    assert result == []


def test_get_file_data_by_path_invalid_json(invalid_json_log_file, capsys):
    result = get_file_data_by_path(invalid_json_log_file)
    assert result == []
    captured = capsys.readouterr()
    assert "Error decoding JSON" in captured.out


def test_get_file_data_by_path_nonexistent_file(nonexistent_file, capsys):
    result = get_file_data_by_path(nonexistent_file)
    assert result == []
    captured = capsys.readouterr()
    assert "doesn't exists" in captured.out


def test_filter_by_date(test_date, sample_log_data):
    filtered = list(filter(partial(filter_by_date, test_date), sample_log_data))
    assert len(filtered) == 3
    for item in filtered:
        assert item["@timestamp"].startswith("2025-05-25")


def test_filter_by_date_no_timestamp(sample_log_data):
    data_without_timestamp = {"url": "/test", "response_time": 0.1}
    assert filter_by_date(date(2025, 5, 25), data_without_timestamp) is False
