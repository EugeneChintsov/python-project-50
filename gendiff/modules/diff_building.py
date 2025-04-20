from typing import Any


def get_diff(first_data: dict[str, Any], second_data: dict[str, Any]) -> dict:
    """
    Compares two dictionaries and returns a diff tree structure
    representing their differences.

    Args:
        first_data (dict): The first dictionary to compare.
        second_data (dict): The second dictionary to compare.

    Returns:
        dict: A nested dictionary (diff tree) where
            each key maps to a dictionary with a 'status' and a 'value'.
            In the case of 'updated', the value is another dict
            with 'removed' and 'added' entries.
    """
    keys = sorted(first_data.keys() | second_data.keys())
    result = {}
    for key in keys:
        if key not in first_data:
            result[key] = {
                'status': 'added',
                'value': second_data.get(key)
            }
        elif key not in second_data:
            result[key] = {
                'status': 'removed',
                'value': first_data.get(key)
            }
        elif (
            isinstance(first_data.get(key), dict)
            and isinstance(second_data.get(key), dict)
        ):
            result[key] = {
                'status': 'nested',
                'value': get_diff(first_data.get(key), second_data.get(key))
            }
        elif first_data.get(key) == second_data.get(key):
            result[key] = {
                'status': 'unchanged',
                'value': first_data.get(key)
            }
        else:
            result[key] = {
                'status': 'updated',
                'value': {
                    'removed': first_data.get(key),
                    'added': second_data.get(key)
                }
            }
    return result