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
        rules[int(line.split(':')[0])] = tuple(line.split('"')[1].split('"')[0])
    else:
        string = line.replace('| ', '')
        string = string.split(': ')[1]
        rules[int(line.split(':')[0])] = tuple(map(int, string.split(' ')))

# Rule 8 --> 42
# Rule 57 --> a
# Rule 58 --> b
# Rule 121 --> a | b
del rules[8]
del rules[57]
del rules[58]
del rules[121]
rules[0] = tuple((42, rules[0][1]))
rev_rules = dict()

for key in rules.keys():
    val_1 = str(rules[key][0]) + ' ' + str(rules[key][1])
    if val_1 not in rev_rules.keys():
        rev_rules[val_1] = tuple((str(key),))
    else:
        rev_rules[val_1] += tuple((str(key),))
    if len(rules[key]) > 2:
        val_2 = str(rules[key][2]) + ' ' + str(rules[key][3])
        if val_2 not in rev_rules.keys():
            rev_rules[val_2] = tuple((str(key),))
        else:
            rev_rules[val_2] += tuple((str(key),))


def analyse_seq(sequence):
    new_seq = []
    for i in range(len(sequence) // 2):
        new_seq.append(tuple())
        for char_1 in sequence[i * 2]:
            for char_2 in sequence[1 + 1 * 2]:
                if char_1 + ' ' + char_2 in rev_rules.keys():
                    new_seq[-1] += rev_rules[char_1 + ' ' + char_2]
        # print(f'new seq --> {new_seq[-1]}')
    for line in new_seq:
        print(line)
    return new_seq.copy()

for key in rev_rules.keys():
    print(f'{key} --> {rev_rules[key]}')

for message in messages:
    seq = []
    for char in message:
        if char == 'a':
            seq.append(('57', '121'))
        elif char == 'b':
            seq.append(('58', '121'))
    while len(seq) != 1:
        seq = analyse_seq(seq.copy())
        breakpoint()
        print(seq)












