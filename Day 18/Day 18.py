import re
with open('input.txt') as f:
    lines = f.read().splitlines()

def solve_eq(string):
    sub = '+*'
    numbers = list(map(int, string.replace('+', '*').split(' * ')))
    operators = list(''.join([i for i in string if i in sub]))
    answer = numbers.pop(0)
    for number in numbers:
        if operators[0] == '*':
            answer *= number
        else:
            answer += number
        del operators[0]
    return answer


def solve_eq_2(string):
    sub = '+*'
    numbers = list(map(int, string.replace('+', '*').split(' * ')))
    operators = list(''.join([i for i in string if i in sub]))
    while '+' in operators:
        index_plus = operators.index('+')
        numbers[index_plus] = numbers[index_plus] + numbers[index_plus + 1]
        del numbers[index_plus + 1]
        del operators[index_plus]
    answer = 1
    for number in numbers:
        answer *= number
    return answer


total_answer = 0

for line in lines:
    while '(' in line:
        for sub_string in (re.findall('\([^()]*\)', line)):
            line = line.replace(sub_string, str(solve_eq(sub_string[1:-1])))
    total_answer += solve_eq(line)

print(f'The answer to part 1 = {total_answer}')

total_answer = 0

for line in lines:
    while '(' in line:
        for sub_string in (re.findall('\([^()]*\)', line)):
            line = line.replace(sub_string, str(solve_eq_2(sub_string[1:-1])))
    total_answer += solve_eq_2(line)

print(f'The answer to part 2 = {total_answer}')