import pytest
from datetime import date
from pathlib import Path
import json
import tempfile


@pytest.fixture
def sample_log_data():
    return [
        {
            "@timestamp": "2025-05-25T12:00:00",
            "url": "/api/users",
            "response_time": 0.2,
            "user_agent": "Chrome",
        },
        {
            "@timestamp": "2025-05-25T12:01:00",
            "url": "/api/users",
            "response_time": 0.3,
        },
        {
            "@timestamp": "2025-05-25T12:02:00",
            "url": "/api/products",
            "response_time": 0.5,
        },
        {
            "@timestamp": "2025-05-26T12:00:00",
            "url": "/api/users",
            "response_time": 0.4,
        },
    ]


@pytest.fixture
def log_file(sample_log_data):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
        for entry in sample_log_data:
            f.write(json.dumps(entry) + "\n")
        f.flush()
        yield Path(f.name)
    Path(f.name).unlink(missing_ok=True)


@pytest.fixture
def empty_log_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
        yield Path(f.name)
    Path(f.name).unlink(missing_ok=True)


@pytest.fixture
def invalid_json_log_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
        f.write('{"invalid": json\n')
        f.write("not a json\n")
        f.flush()
        yield Path(f.name)
    Path(f.name).unlink(missing_ok=True)


@pytest.fixture
def nonexistent_file():
    return Path("nonexistent_file.log")


@pytest.fixture
def test_date():
    return date(2025, 5, 25)
