from typing import Any, Dict
import json
 

def format_value(value: Any) -> str:
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool | None):
        return json.dumps(value)
    return f"'{value}'"


def walk_tree(data: dict, parent_path: str='') -> str:
    lines = []
    for key, val in data.items():
        status = val.get('status')
        value = val.get('value')
        
        if parent_path:
            current_path = f'{parent_path}.{key}'
        else:
            current_path = f'{key}'
        
        if status == 'nested':
            lines.append(f'{walk_tree(value, current_path)}')
        
        elif status == 'added':
            lines.append(
                f"Property '{current_path}' was added "
                f"with value: {format_value(value)}"
            )
        
        elif status == 'deleted':
            lines.append(f"Property '{current_path}' was removed")

        elif status == 'changed':
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {format_value(value['deleted'])} "
                f"to {format_value(value['added'])}"
            )
        
    return '\n'.join(lines)

def apply_plain(data: Dict[str, Any]) -> str:
    return walk_tree(data)


# Property 'common.follow' was added with value: false
# Property 'common.setting2' was removed
# Property 'common.setting3' was updated. From true to null
# Property 'common.setting4' was added with value: 'blah blah'
# Property 'common.setting5' was added with value: [complex value]
# Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
# Property 'common.setting6.ops' was added with value: 'vops'
# Property 'group1.baz' was updated. From 'bas' to 'bars'
# Property 'group1.nest' was updated. From [complex value] to 'str'
# Property 'group2' was removed
# Property 'group3' was added with value: [complex value]