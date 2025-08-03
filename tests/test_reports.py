from app.reports.average import ReporterAverage
from app.reports.base import BaseReporter
import pytest


def test_base_reporter_abstract_method():
    with pytest.raises(TypeError):
        BaseReporter()


def test_average_reporter(sample_log_data, capsys):
    reporter = ReporterAverage(sample_log_data)
    captured = capsys.readouterr()
    assert "/api/users" in captured.out
    assert "/api/products" in captured.out
    assert "avg. reponse time" in captured.out
    assert "0.3" in captured.out  # avg for /api/users
    assert "1" in captured.out  # count for /api/products


def test_average_reporter_empty_data(capsys):
    reporter = ReporterAverage([])
    captured = capsys.readouterr()
    assert captured.out.strip() == ""  # No output for empty data


# def test_user_agent_reporter_placeholder(sample_log_data):
#     from app.reports.user_agent import ReporterUserAgent
#     assert ReporterUserAgent(sample_log_data)
