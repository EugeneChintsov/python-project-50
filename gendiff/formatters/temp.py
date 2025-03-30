from typing import Any, Dict
import json
import itertools


MAPPING = {
    'added': '+ ',
    'deleted': '- ',
    'unchanged': '  '
} 
REPLACER = ' '
REPLACER_COUNT = 2 # вспомнить почему тут 2


def get_indent(depth: int) -> tuple[int, str]:
    depth_size = depth * REPLACER_COUNT * 2
    depth_indent = REPLACER * depth_size
    return depth_size, depth_indent

def format_value_to_string(value: Any) -> str:
    if isinstance(value, bool | None):
        return json.dumps(value)
    return str(value)


def format_value(value: Any, depth: int) -> str:
    if not isinstance(value, dict):
        return format_value_to_string(value)
    
    depth_size, depth_indent = get_indent(depth)
    
    lines = []
    for key, val in value.items():
        lines.append(f'{depth_indent}  {key}: {format_value(val, depth_size)}')
        
    current_indent = REPLACER * (REPLACER_COUNT * depth)
    result = itertools.chain('{', lines, current_indent + '}')  # mb like this [current_indent + "}"]
    return '\n'.join(result)


def walk_tree(data: dict, depth:int) -> str:
    next_depth, current_indent = get_indent(depth)

    lines = []
    for key, val in data.items():
        status = val.get('status')
        value = val.get('value')

        if status in MAPPING:
            lines.append(
                f'{current_indent}{MAPPING.get(status)}{key}: {format_value(value, next_depth)}'
                )
        
        elif status == 'changed':
            lines.append(f'{current_indent}{MAPPING.get("added")}{key}: {format_value(value["added"], next_depth)}')
            lines.append(f'{current_indent}{MAPPING.get("deleted")}{key}: {format_value(value["deleted"], next_depth)}')

        if status == 'nested':
            lines.append(f'{current_indent}  {key}: {walk_tree(value, next_depth)}')

    current_indent = REPLACER * (REPLACER_COUNT * depth)
    result = itertools.chain('{', lines, [current_indent + '}'])  # mb like this [current_indent + "}"]
    return '\n'.join(result)


def apply_stylish(data: Dict[str, Any]) -> str:
    return walk_tree(data, -REPLACER_COUNT)


#вместо очень длинной f строки
# '{first} {second}'.format(
#     first=1,
#     second=2,
# )