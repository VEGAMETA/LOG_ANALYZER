from app.processor import Processor
from unittest.mock import patch, MagicMock


def test_processor_with_valid_args(log_file, capsys):
    with patch("app.processor.Parser") as mock_parser:
        mock_args = MagicMock()
        mock_args.file = [str(log_file)]
        mock_args.report = "average"
        mock_args.date = None
        mock_parser.return_value.parse_args.return_value = mock_args

        processor = Processor()
        captured = capsys.readouterr()
        assert "/api/users" in captured.out
        assert "avg. reponse time" in captured.out


def test_processor_empty_data(empty_log_file, capsys):
    with patch("app.processor.Parser") as mock_parser:
        mock_args = MagicMock()
        mock_args.file = [str(empty_log_file)]
        mock_args.report = "average"
        mock_args.date = None
        mock_parser.return_value.parse_args.return_value = mock_args

        processor = Processor()
        captured = capsys.readouterr()
        assert "Nothing to report" in captured.out


def test_processor_invalid_report_type(log_file, capsys):
    with patch("app.processor.Parser") as mock_parser:
        mock_args = MagicMock()
        mock_args.file = [str(log_file)]
        mock_args.report = "invalid_report"
        mock_args.date = None
        mock_parser.return_value.parse_args.return_value = mock_args

        processor = Processor()
        captured = capsys.readouterr()
        assert "Invalid report type" in captured.out
