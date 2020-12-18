with open('input.txt') as f:
    lines = f.read().splitlines()

correct_passwords_1 = 0
correct_passwords_2 = 0

for line in lines:
    password = line.split(' ')[-1]
    letter = line.split(':')[0].split(' ')[-1]
    minimum = int(line.split('-')[0])
    maximum = int(line.split('-')[1].split(' ')[0])
    if minimum <= password.count(letter) <= maximum:
        correct_passwords_1 += 1
    if (password[minimum - 1] + password[maximum - 1]).count(letter) == 1:
        correct_passwords_2 += 1

print(f'There are {len(lines)} passwords in total')
print(f'There are {correct_passwords_1} correct passwords for part 1')
print(f'There are {correct_passwords_2} correct passwords for part 2')
