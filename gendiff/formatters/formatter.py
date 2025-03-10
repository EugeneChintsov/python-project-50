from typing import Dict, Any
from gendiff.formatters.json import apply_json
from gendiff.formatters.plain import apply_plain
from gendiff.formatters.stylish import apply_stylish



def apply_formatter(data: Dict[str, Any], format: str) -> str:
    if format == 'json':
        return apply_json(data)
    if format == 'plain':
        return apply_plain(data)
    if format == 'special':
        return apply_stylish(data)