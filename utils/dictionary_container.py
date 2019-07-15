# Code by ByungWook.Kang @lesimor
import pprint
from typing import Any
from utils.object import ObjectUtil

PP = pprint.PrettyPrinter(indent=2)


class DictionaryContainer:
    """Dictionary data handler."""

    def __init__(self, data: dict):
        if not (isinstance(data, dict)):
            raise ValueError(PP.pformat(data))
        self._data = data

    def get(self, *paths) -> Any:
        """Dictionary getter method"""
        value, found = ObjectUtil.get_from_path(self._data, '.'.join(paths))
        return value

    def set(self, path: str, value: Any) -> None:
        """Dictionary setter method"""
        paths = path.split('.')
        dic = self._data
        for path in paths[:-1]:
            dic = dic.setdefault(path, {})
        dic[paths[-1]] = value

    def to_dict(self) -> dict:
        return self._data

    def __str__(self):
        """Stringifier"""
        return PP.pformat(self._data)
