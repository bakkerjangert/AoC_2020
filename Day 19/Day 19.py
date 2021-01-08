import re
with open('input.txt') as f:
    lines = f.read().splitlines()


def get_re(string):
    regex_list = tuple(string)
    while True:
        check = [ele for ele in replacements if(ele in regex_list)]
        if len(check) == 0:
            break
        for val in check[::-1]:
            val_index = regex_list.index(val)
            regex_list = regex_list[: val_index] + rules[val] + regex_list[val_index + 1:]
    return ''.join(regex_list)


def get_re_2(string):
    strings = set()
    unfinished_strings = [(string,)]
    while len(unfinished_strings) > 0:
        cur_string = unfinished_strings.pop(0)
        while True:
            for item in cur_string:
                if item in rules.keys():
                    index = cur_string.index(item)
                    rule = rules[item]
                    if item == '57' or item == '58':
                        cur_string = cur_string[:index] + (rule[0],) + cur_string[index + 1:]
                        break
                    elif '|' in rule and len(rule) == 7:
                        unfinished_strings.append(cur_string[:index] + (rule[4], rule[5],) + cur_string[index + 1:])
                        cur_string = cur_string[:index] + (rule[1], rule[2],) + cur_string[index + 1:]

                        break
                    elif '|' in rules[item]:
                        unfinished_strings.append(cur_string[:index] + (rule[3],) + cur_string[index + 1:])
                        cur_string = cur_string[:index] + (rule[1],) + cur_string[index + 1:]
                        break
                    else:
                        cur_string = cur_string[:index] + (rules[item][1],) + (rules[item][2],) + cur_string[index + 1:]
                        break
            if cur_string.count('a') + cur_string.count('b') == len(cur_string):
                strings.add(''.join(cur_string))
                break
    return strings

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

replacements = tuple(rules.keys())
reg_check = re.compile(get_re('0'))
answer = set()

for message in messages:
    if reg_check.fullmatch(message) is not None:
        answer.add(message)

print(f'The answer to part 1 = {len(answer)}')

answer = 0
regex_42 = get_re_2('42')
regex_31 = get_re_2('31')

for message in messages:
    # print(f'--- Message = {message} ---')
    end_42 = False
    count_42 = 0
    count_31 = 0
    for i in range(len(message) // 8):
        if len(message) < 24:
            break
        sub_message = message[0 + i*8: 8 + i*8]
        # print(sub_message)
        if i == 0 or i == 1:
            if sub_message not in regex_42:
                break
            # print('Rule 42 found (1st 2 entries)')
            count_42 += 1
        elif i == len(message) // 8 - 1:
            if sub_message not in regex_31:
                break
            count_31 += 1
            if count_42 - 1 < count_31:
                # print('Rule 31 found (last entrie) --> but too many rules 31 compared to 42')
                break
            # print('Rule 31 found (last entrie) --> answer + 1')
            answer += 1
        elif (sub_message in regex_42) and (not end_42):
            # print('Rule 42 found (midsection)')
            count_42 += 1
            continue
        elif sub_message in regex_31:
            # print('Rule 31 found (midsection)')
            count_31 += 1
            end_42 = True
            continue
        else:
            break

print(f'The answer to part 2 = {answer}')

