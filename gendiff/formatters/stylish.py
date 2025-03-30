from typing import Any, Dict
import json
import itertools


MAPPING = {
    'added': '+ ',
    'deleted': '- ',
    'unchanged': '  '
} 
REPLACER = ' '
REPLACER_COUNT = 4


def get_indent(depth: int) -> tuple[int, str, int]:
    """
    Вычисляет отступы для текущего и следующего уровня вложенности.

    Args:
        depth (int): Текущий уровень вложенности.

    Returns:
        tuple[str, str, int]: 
            - indent (str): Отступ для текущего уровня.
            - deep_indent (str): Отступ для следующего уровня.
            - next_depth (int): Следующий уровень вложенности.
    """
    depth_size = depth * REPLACER_COUNT 
    indent = REPLACER * depth_size
    deep_indent = REPLACER * (depth_size + REPLACER_COUNT)
    next_depth = depth + 1
    return indent, deep_indent, next_depth


def format_value(value: Any) -> str:
    """
    Преобразует переданное значение в строку.

    Args:
        value (Any): Значение любого типа.

    Returns:
        str: Строковое представление значения.
    """
    if isinstance(value, bool | None):
        return json.dumps(value)
    return str(value)


def format_dict(value: Any, depth: int) -> str:
    """
    Форматирует словарь в строку с отступами.

    Args:
        value (Any): Значение, которое нужно отформатировать. Если это не словарь, 
                     будет вызвана функция format_value().
        depth (int): Текущая глубина вложенности для корректного расчета отступов.

    Returns:
        str: Форматированное строковое представление словаря.
    """
    if not isinstance(value, dict):
        return format_value(value)
    
    indent, deep_indent, next_depth = get_indent(depth)
    lines = []
    for key, val in value.items():
        lines.append(f'{deep_indent}{key}: {format_dict(val, next_depth)}')
        
    result = itertools.chain('{', lines, [indent + '}'])
    return '\n'.join(result)


def walk_tree(data: dict, depth:int) -> str:
    """
    Проходит по дереву данных и формирует строковое представление с отступами.

    Эта функция используется для рекурсивного обхода
    вложенных структур данных (словарей),
    применяя отступы для каждого уровня вложенности.

    Args:
        data (dict): Данные, которые нужно обработать. Словарь,
                     где ключи — это имена атрибутов,
                     а значения — их статусы и вложенные данные.
        depth (int): Текущий уровень вложенности.
                     Используется для вычисления отступов.

    Returns:
        str: Строковое представление данных с учетом изменений, добавлений,
                удалений и вложенных данных.
    """
    indent, deep_indent, next_depth = get_indent(depth)
    lines = []
    for key, val in data.items():
        status = val.get('status')
        value = val.get('value')

        if status in MAPPING:
            lines.append(
                f'{indent}  {MAPPING.get(status)}{key}: {format_dict(value, next_depth)}'
                )
        
        elif status == 'changed':
            lines.append(f'{indent}  {MAPPING.get("added")}{key}: {format_dict(value["added"], next_depth)}')
            lines.append(f'{indent}  {MAPPING.get("deleted")}{key}: {format_dict(value["deleted"], next_depth)}')

        if status == 'nested':
            lines.append(f'{deep_indent}{key}: {walk_tree(value, next_depth)}')

    result = itertools.chain('{', lines, [indent + '}'])
    return '\n'.join(result)


def apply_stylish(data: Dict[str, Any]) -> str:
    """
    Применяет стиль к данным, обходя их с заданным уровнем вложенности
    и возвращая строку в нужном формате.

    Эта функция вызывает функцию `walk_tree` для обработки данных с начальной глубиной 0, 
    формируя строковое представление данных с нужными отступами и форматированием.

    Args:
        data (dict): Данные для обработки. Словарь с атрибутами, значениями и статусами изменений.

    Returns:
        str: Строковое представление данных, отформатированное с учетом изменений и вложенных структур.
    """
    return walk_tree(data, 0)
