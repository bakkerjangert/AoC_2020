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
        rules[int(line.split(':')[0])] = tuple(line.split('"')[1].split('"')[0])
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

for_zero = {1: set()}
zero_index = 1
temp = []
sequence = [0]

while True:
    for i in range(len(sequence)):
        change = False
        val_1 = sequence[i]
        if val_1 == 'a' or val_1 == 'b':
            pass
        else:
            change = True
            new_sequence = sequence.copy()
            next_rule = list(rules[val_1])
            index = new_sequence.index(val_1)
            if len(next_rule) == 4:
                new_sequence_2 = new_sequence.copy()
                del new_sequence_2[index]
                for j in range(2):
                    new_sequence_2.insert(index, next_rule.pop(-1))
                temp.append(new_sequence_2.copy())
            del new_sequence[index]
            while len(next_rule) > 0:
                new_sequence.insert(index, next_rule.pop(-1))
            break
    if change:
        sequence = new_sequence.copy()
    if sequence.count('a') + sequence.count('b') == len(sequence):
        if len(for_zero[zero_index]) > 9999:
            zero_index += 1
            for_zero[zero_index] = set()

        for_zero[zero_index].add(''.join(sequence))
        if len(temp) != 0:
            sequence = temp.pop(0).copy()
        else:
            break

answer = 0

for message in messages:
    for sub_set in for_zero.values():
        if message in sub_set:
            answer += 1
            break

print(f'The answer to part 1 = {answer}')

# Wrong answer = 26,