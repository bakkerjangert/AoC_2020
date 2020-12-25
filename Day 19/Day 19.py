import re
with open('input.txt') as f:
    lines = f.read().splitlines()

rules = dict()
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
        rules[(line.split(':')[0])] = tuple(line.split('"')[1].split('"')[0])
    else:
        string = line.split(': ')[1]
        rules[line.split(':')[0]] = tuple('(') + tuple(tuple(string.split(' '))) + tuple(')')

regex_list = tuple('0')
replacements = tuple(rules.keys())

while True:
    check = [ele for ele in replacements if(ele in regex_list)]
    if len(check) == 0:
        break
    for val in check[::-1]:
        val_index = regex_list.index(val)
        regex_list = regex_list[: val_index] + rules[val] + regex_list[val_index + 1:]

reg_check = re.compile(''.join(regex_list))
print(''.join(regex_list))
answer = 0

for message in messages:
    if reg_check.fullmatch(message) is not None:
        answer += 1

print(f'The answer to part 1 = {answer}')
