with open('input.txt') as f:
    lines = f.read().splitlines()

valid_numbers = set()
ordered_numbers = dict()

for line in lines:
    if line == '':
        break
    row_numbers = []
    start_1 = int(line.split(': ')[1].split('-')[0])
    start_2 = int(line.split('or ')[1].split('-')[0])
    end_1 = int(line.split('-')[1].split(' or')[0])
    end_2 = int(line.split('or ')[1].split('-')[1])
    for i in range(start_1, end_1 + 1):
        valid_numbers.add(i)
        row_numbers.append(i)
    for j in range(start_2, end_2 + 1):
        valid_numbers.add(j)
        row_numbers.append(j)
    ordered_numbers[line.split(':')[0]] = tuple(row_numbers)

check = False
invalid_numbers = []
valid_tickets = []
my_ticket = None
next_is_my_ticket = False

for line in lines:
    if line == 'your ticket:':
        next_is_my_ticket = True
        continue
    if next_is_my_ticket:
        my_ticket = tuple(map(int, line.split(',')))
        next_is_my_ticket = False
    if line == 'nearby tickets:':
        check = True
        continue
    if check:
        valid = True
        numbers = tuple(map(int, line.split(',')))
        for number in numbers:
            if number not in valid_numbers:
                valid = False
                invalid_numbers.append(number)
        if valid:
            valid_tickets.append(numbers)

print(f'The answer to part 1 = {sum(invalid_numbers)}')

fields = []
real_fields = []
number_of_valid_tickets = len(valid_tickets)

for i in range(len(my_ticket)):
    fields.append([])
    for ticket in valid_tickets:
        for key in ordered_numbers.keys():
            if ticket[i] in ordered_numbers[key]:
                fields[-1].append(key)
    real_field = []
    for field in fields[-1]:
        if fields[-1].count(field) == number_of_valid_tickets:
            real_field.append(field)
    real_fields.append(tuple(real_field))

check_list = list(ordered_numbers.keys())
i = 0

while len(check_list) != 0:
    check_field = check_list[i]
    count = 0
    for j in range(len(real_fields)):
        if check_field in real_fields[j]:
            count += 1
            field_data = (check_field, j)
        if count == 2:
            i += 1
            break
    if count == 1:
        real_fields[field_data[1]] = (field_data[0])
        check_list.remove(check_field)
        i = 0

answer = 1

for i in range(len(real_fields)):
    # print(real_fields[i])
    if 'departure' in real_fields[i]:
        answer *= my_ticket[i]

print(f'The answer to part 2 = {answer}')
