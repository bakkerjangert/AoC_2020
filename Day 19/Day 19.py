import re
with open('input.txt') as f:
    lines = f.read().splitlines()

rules = dict()
encoded = dict()
messages = list()

add_messages = False

for line in lines:
    if line == '':
        add_messages = True
        continue
    if add_messages:
        messages.append(line)
        continue
    if '"' in line:
        encoded[int(line.split(':')[0])] = tuple(line.split('"')[1].split('"')[0])
    else:
        string = line.replace('| ', '')
        string = string.split(': ')[1]
        rules[int(line.split(':')[0])] = tuple(map(int, string.split(' ')))


def decode(x, y):
    solution = set()
    for x_sub in x:
        for y_sub in y:
            solution.add(x_sub + y_sub)
            # print(x_sub + y_sub)
    return solution


while 0 not in encoded.keys():
    new_rules = rules.copy()
    for key in rules.keys():
        check = True
        for number in rules[key]:
            if number not in encoded.keys():
                check = False
                break
        if check:
            sub_set = list()
            check_numbers = rules[key]
            del new_rules[key]
            if len(check_numbers) == 1:
                encoded[key] = rules[check_numbers[0]]
            else:
                for i in range(len(check_numbers) // 2):
                    val_1, val_2 = encoded[check_numbers[0 + 2 * i]], encoded[check_numbers[0 + 2 * i]]
                    for item in decode(val_1, val_2):
                        sub_set.append(item)
            encoded[key] = set(sub_set)
    rules = new_rules.copy()
    for key in encoded.keys():
        print(key, encoded[key])


# for item in rules.items():
#     if len(item[1]) == 3:
#         print('THERE IS A 3!!!')
#     print(item)
#
# for item in encoded.items():
#     print(item)