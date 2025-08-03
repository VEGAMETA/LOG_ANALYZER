from abc import ABC, abstractclassmethod


class BaseFormatter(ABC):
    @abstractclassmethod
    def format(cls, data, **kwargs) -> None: ...
