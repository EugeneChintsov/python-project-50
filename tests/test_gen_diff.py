import os

import pytest

from gendiff import generate_diff


def file_path(file_name: str) -> str:
    """Returns the absolute path to a fixture file."""
    fixtures_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    'fixtures'
    )
    return os.path.join(fixtures_path, file_name)


def get_expected(file_name: str) -> str:
    """Reads the expected result from a file and strips trailing whitespace."""
    with open(file_path(file_name)) as f:
        return f.read().strip()


@pytest.mark.parametrize(
        "first_file, second_file, format, expected",
        [
            ("file1.json", "file2.json", "stylish", "result_stylish"),
            ("file1.json", "file2.json", "plain", "result_plain"),
            ("file1.json", "file2.json", "json", "result_json"),
            ("file1.yml", "file2.yml", "json", "result_json"),
            ("file1.yml", "file2.yml", "stylish", "result_stylish"),
            ("file1.yml", "file2.yml", "plain", "result_plain"),
        ]
)
def test_gen_diff(
    first_file: str, second_file: str, format: str, expected: str
) -> None:
    """Tests the `generate_diff` function with different input formats."""
    result = generate_diff(
        file_path(first_file),
        file_path(second_file),
        format
    )
    assert result == get_expected(expected)
