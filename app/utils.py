import inspect

from pathlib import Path
from json import loads, JSONDecodeError
from typing import Iterator
from datetime import datetime

from . import reports


def get_reporters() -> Iterator[str]:
    for _, obj in inspect.getmembers(reports):
        if not inspect.isclass(obj):
            continue
        if not hasattr(obj, "report_type"):
            continue
        yield obj


reporters = {obj.report_type: obj for obj in get_reporters()}


def get_file_data_by_path(path: str) -> list[dict]:
    filepath = Path(path)
    data = []
    try:
        if not filepath.is_file():
            raise FileExistsError
        with open(filepath) as f:
            for line in f:
                data.append(loads(line))
    except JSONDecodeError as e:
        print(f"Error decoding JSON from {path}: {e}")
    except FileExistsError:
        print(f"File {path} doesn't exists")
    except Exception as e:
        print(f"Unexpected error reading {path}: {e}")
    finally:
        return data


def filter_by_date(filter_date: datetime, chunk) -> bool:
    request_time = chunk.get("@timestamp")
    if not request_time:
        return False
    return filter_date == datetime.fromisoformat(request_time).date()
