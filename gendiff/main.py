from gendiff.modules.file_parsing import get_data
from gendiff.formatters.formatter import formatter
from gendiff.modules.diff_building import get_diff
from typing import Any   

def generate_diff(first_file: str, second_file:str, format:str) -> Any:
    """
     Generates a difference report between two configuration files.
    """
    diff = get_diff(get_data(first_file),get_data(second_file))
    return formatter(diff, format)