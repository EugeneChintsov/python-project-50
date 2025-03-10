import json
import yaml
# Определить формат файла , если неправильный формат - выкинуть ошибку 
# применить метод(парсить)
# получить данные


def get_file_type(file_full_name: str) -> str:
    """
     Determines the type of file based on its extension.
    """
    if file_full_name.endswith('.json'):
        return 'json'
    elif file_full_name.endswith(('.yml', '.yaml')):
        return 'yaml'
    return None
    # TO DO: raise
    # print(f"Ошибка: неподдерживаемый формат файла '{file_full_name}'")


def parse_data(data: str, file_type: str) -> dict:
    """
    Parses data from a given string based on the specified file type.
    """
    if file_type == 'json':
        return json.loads(data)
    elif file_type == 'yaml':
        return yaml.safe_load(data)
    else:
         return None    
        # TO DO: raise  и тогда возвращаемый тип данных будет dict
        # print("Ошибка: Некорректный JSON-файл.")
        # print("Ошибка: Некорректный YAML-файл.")


def get_data(file_full_name: str) -> dict: 
    """
    Retrieves and parses data from a file based on its format.
    """
    file_type = get_file_type(file_full_name)
    with open(file_full_name, "r", encoding="utf-8") as file:
        data = file.read()
        return parse_data(data, file_type)

    # TO DO: raise
    # print(f"Ошибка: Файл '{file_full_name}' не найден.")