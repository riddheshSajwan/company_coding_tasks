#jagan.sivam@skit.ai
def redact_dict(input, path):
    # TODO: implement
    nested_path = path.split('.')
    input_temp = input
    for i in range(len(nested_path)):
        key = nested_path[i]
        if type(input_temp) == set:
            return
        elif key == "*":
            break
        elif type(input_temp) == list and key.isdigit():
            index = int(key)
            if i == len(nested_path)-1:
                if index < len(input_temp):
                    input_temp[index] = "*"*len(str(input_temp[index]))
                return
            else:
                input_temp = input_temp[index]
        elif type(input_temp) == dict and key in input_temp:
            if i == len(nested_path)-1:
                input_temp[key] = "*"*len(key)
            else:
                input_temp = input_temp[key]
        else:
            return
    if type(input_temp) == dict:
        return
    elif type(input_temp) == list:
        for i in range(len(input_temp)):
            input_temp[i] = "*"*len(str(input_temp[i]))
    elif type(input_temp) == set:
        for item in input_temp:
            input_temp.remove(item)
            input_temp.add("*"*len(str(item)))




if __name__ == '__main__':
    input = {
        'm1': {
            'm2': {
                'm3': 55
            }
        },
        'm4': [False, 'bb', 'ccc'],
        'm6': ['a', 'b', 'c']
    }

    paths = [
        'm1.m2.m3',
        'm2.m5',
        'm4.*',
        'm4.*.k9',
        'm6.2',
        'm6.2000',
    ]
    k = input
    for path in paths:
        redact_dict(input, path)
        #print(k)

    assert k == {
        'm1': {
            'm2': {
                'm3': "**"
            }
        },
        'm4': ['*****', '**', '***'],
        'm6': ['a', 'b', '*']
    }