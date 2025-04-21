import json
from typing import Any


def format_value(value: Any) -> str:
    """
    Formats a value into a string suitable for plain-text output.

    Args:
        value (Any): The value to be formatted.

    Returns:
        str: A string representation of the value.
    """
    if isinstance(value, dict):
        return '[complex value]'
    
    elif isinstance(value, bool | None):
        return json.dumps(value)
    
    elif isinstance(value, int | float):
        return str(value)

    return f"'{value}'"


def walk_tree(data: dict[str, Any], parent_path: str = '') -> str:
    """
    Recursively traverses a dictionary representing a difference tree 
    and returns a plain-text description of changes.

    Args:
        data (dict): A dictionary representing a diff tree.
                    Each key corresponds to a property, and its value is a dict
                    containing a 'status' and associated value(s).
        parent_path (str, optional): A dot-separated path
                                    representing the nesting 
                                    hierarchy of keys. Defaults to ''.

    Returns:
        str: A string describing the changes in a plain, readable format.
    """
    lines = []
    for key, val in data.items():
        status = val.get('status')
        value = val.get('value')
        
        current_path = f'{parent_path}.{key}' if parent_path else key
        template = f"Property '{current_path}' was {status}"
        
        if status == 'nested':
            lines.append(walk_tree(value, current_path))
        
        elif status == 'added':
            lines.append(f"{template} with value: {format_value(value)}")
        
        elif status == 'removed':
            lines.append(template)

        elif status == 'updated':
            removed = format_value(value['removed'])
            added = format_value(value['added'])
            lines.append(f"{template}. From {removed} to {added}")

    return '\n'.join(lines)


def apply_plain(data: dict[str, Any]) -> str:
    """
    Formats a given diff tree into a plain text representation.

    Args:
        data (dict): A dictionary representing a diff tree.
    Returns:
        str: A string describing the changes in a plain, readble format.
    """
    return walk_tree(data)
