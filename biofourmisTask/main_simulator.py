import json
from Value_Generator import generate_data
from os.path import exists


for ts in range(3600):
    if exists("sample.json"):
        with open("sample.json", 'r') as file:
            data_list = json.load(file)
            data_list += generate_data("abc", ts)
        with open("sample.json", 'w') as file:
            json.dump(data_list, file)
    else:
        with open("sample.json", 'w+') as file:
            json.dump(generate_data("abc", ts), file)