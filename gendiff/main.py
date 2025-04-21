from typing import Any, Optional

from gendiff.formatters.formatter import apply_formatter
from gendiff.modules.diff_building import get_diff
from gendiff.modules.file_parsing import get_data


def generate_diff(
        first_file: str,
        second_file: str,
        format: Optional[str] = "stylish",
    ) -> Any:
    """
     Generates a difference report between two configuration files.
    """
    diff = get_diff(get_data(first_file), get_data(second_file))
    return apply_formatter(diff, format)