from typing import Any, Dict

from gendiff.formatters.json_ import apply_json
from gendiff.formatters.plain import apply_plain
from gendiff.formatters.stylish import apply_stylish


def apply_formatter(data: Dict[str, Any], format: str) -> str:
    if format == 'json':
        return apply_json(data)
    if format == 'plain':
        return apply_plain(data)
    if format == 'stylish':
        return apply_stylish(data)