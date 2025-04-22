import json

import yaml


def get_file_type(file_full_name: str) -> str:
    """
     Determines the type of file based on its extension.
    """
    if file_full_name.endswith('.json'):
        return 'json'
    elif file_full_name.endswith(('.yml', '.yaml')):
        return 'yaml'
    raise ValueError(
        f"Ошибка: неподдерживаемый формат файла '{file_full_name}'"
    ) 


def parse_data(data: str, file_type: str) -> dict:
    """
    Parses data from a given string based on the specified file type.
    """
    if file_type == 'json':
        return json.loads(data)
    elif file_type == 'yaml':
        return yaml.safe_load(data)


def get_data(file_full_name: str) -> str: 
    """
    Retrieves and parses data from a file based on its format.
    """
    with open(file_full_name, "r", encoding="utf-8") as file:
        return file.read()
