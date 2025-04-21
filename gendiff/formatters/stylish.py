import itertools
import json
from typing import Any

MAPPING = {
    'added': '  + ',
    'removed': '  - ',
    'unchanged': '    ',
}

REPLACER = ' '
REPLACER_COUNT = 4
TEMPLATE = '{indent}{key}: {formated_value}'


def get_indent(depth: int) -> tuple[str, str]:
    """
    Calculates the indentation strings for the current
    and the next nesting levels.

    Args:
        depth (int): The current nesting level.

    Returns:
        tuple[str, str]:
            - indent (str): Indentation for the current level.
            - deep_indent (str): Indentation for the next (deeper) level.
    """
    depth_size = depth * REPLACER_COUNT 
    indent = REPLACER * depth_size
    deep_indent = REPLACER * (depth_size + REPLACER_COUNT)
    return indent, deep_indent


def format_value(value: Any) -> str:
    """
    Converts the given value to its string representation.

    Args:
        value (Any): A value of any type.

    Returns:
        str: The string representation of the value.
    """
    if isinstance(value, bool | None):
        return json.dumps(value)

    return str(value)


def format_dict(value: dict[str, Any], depth: int) -> str:
    """
    Formats a dictionary into a properly indented string.

    Args:
        value (Any): The value to be formatted. If it's not a dictionary,
                     the format_value() function will be used instead.
        depth (int): The current nesting depth, used to calculate indentation.

    Returns:
        str: A formatted string representation of the dictionary.
    """
    if not isinstance(value, dict):
        return format_value(value)
    
    indent, deep_indent = get_indent(depth)
    next_depth = depth + 1
    lines = []
    for key, val in value.items():
        lines.append(
            TEMPLATE.format(
                indent=deep_indent,
                key=key,
                formated_value=format_dict(val, next_depth),
            )
        )
        
    result = itertools.chain('{', lines, [indent + '}'])
    return '\n'.join(result)


def walk_tree(data: dict[str, Any], depth: int) -> str:
    """
    Traverses a tree-like data structure
    and generates a formatted string with indentation.

    Args:
        data (dict): The data to process.
                     A dictionary where keys represent attribute names,
                     and values contain their status
                     and potentially nested data.
        depth (int): The current level of nesting,
                     used to calculate indentation.

    Returns:
        str: A formatted string representation of the data,
             reflecting added, removed, updated, and nested values.
    """
    indent, deep_indent = get_indent(depth)
    next_depth = depth + 1
    lines = []
    for key, val in data.items():
        status = val.get('status')
        value = val.get('value')

        if status in MAPPING:
            lines.append(
                TEMPLATE.format(
                    indent=indent + MAPPING.get(status),
                    key=key,
                    formated_value=format_dict(value, next_depth),
                )            
            )
        
        elif status == 'updated':
            lines.append(
                TEMPLATE.format(
                    indent=indent + MAPPING.get("added"),
                    key=key,
                    formated_value=format_dict(value["added"], next_depth),
                )
            )
            lines.append(
                TEMPLATE.format(
                    indent=indent + MAPPING.get("removed"),
                    key=key,
                    formated_value=format_dict(value["removed"], next_depth),
                )
            )

        elif status == 'nested':
            lines.append(
                TEMPLATE.format(
                    indent=deep_indent,
                    key=key,
                    formated_value=walk_tree(value, next_depth),
                )
            )

    result = itertools.chain('{', lines, [indent + '}'])
    return '\n'.join(result)


def apply_stylish(data: dict[str, Any]) -> str:
    """
    Applies formatting style to the data by recursively traversing it
    and returning a properly formatted string representation.

    Args:
        data (dict): The data to process. A dictionary containing attributes,
                     their values, and change statuses.

    Returns:
        str: A formatted string representation of the data,
             including changes and nested structures.
    """
    return walk_tree(data, depth=0)
