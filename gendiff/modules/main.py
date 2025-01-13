import json


def generate_diff(data):
    args = data()
    dict1 = json.load(open(args.first_file))
    dict2 = json.load(open(args.second_file))
    # format = args.format
    print(dict1)
    print(dict2)
    final_result = ''
    return final_result