def get_diff(first_data: dict, second_data: dict) -> dict:
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
                'status': 'deleted',
                'value': first_data.get(key)
            }
        elif (isinstance(first_data.get(key), dict) and isinstance(second_data.get(key), dict)):
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
                'status': 'changed',
                'value': {
                    'deleted': first_data.get(key),
                    'added': second_data.get(key)
                }
            }
    return result