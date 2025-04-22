from typing import Any, Optional

from gendiff.formatters.formatter import apply_formatter
from gendiff.modules.diff_building import get_diff
from gendiff.modules.file_parsing import get_data, get_file_type, parse_data


def generate_diff(
    first_file: str,
    second_file: str,
    format: Optional[str] = "stylish",
) -> Any:
    """
     Generates a difference report between two configuration files.
    """
    first_file_type, first_data = (
        get_file_type(first_file),
        get_data(first_file),
    )
    second_file_type, second_data = (
        get_file_type(second_file),
        get_data(second_file),
    )
    first_parsed_data = parse_data(first_data, first_file_type)
    second_parsed_data = parse_data(second_data, second_file_type)
    
    return apply_formatter(
        get_diff(
            first_parsed_data,
            second_parsed_data,
        ),
        format,
    )