def print_sequence(cup):
    org_cup = cup
    print(cup, end=', ')
    cup = cups[cup]
    while cup != org_cup:
        print(cup, end=', ')
        cup = cups[cup]
    print('')


data = '364289715'
# Testdata
# data = '389125467'

cups = dict()

for i in range(len(data)):
    val_1 = int(data[i])
    if i != len(data) - 1:
        val_2 = int(data[i + 1])
    else:
        val_2 = int(data[0])
    cups[val_1] = val_2

cup = int(data[0])
max_val = max(cups.keys())

for move in range(100):
    # print_sequence(cup)
    cup_1 = cups[cup]
    cup_2 = cups[cup_1]
    cup_3 = cups[cup_2]
    destination_cup = cup - 1
    while destination_cup in (cup_1, cup_2, cup_3, 0):
        if destination_cup == 0:
            destination_cup = max_val
        else:
            destination_cup -= 1
    cups[cup] = cups[cup_3]
    cups[cup_3] = cups[destination_cup]
    cups[destination_cup] = cup_1
    cup = cups[cup]

print('The anwer to part 1 = ', end='')
final_cup = cups[1]
while final_cup != 1:
    print(final_cup, end='')
    final_cup = cups[final_cup]
print('')

# Part 2
cups = dict()
for i in range(len(data)):
    val_1 = int(data[i])
    if i != len(data) - 1:
        val_2 = int(data[i + 1])
    else:
        val_2 = int(data[0])
    cups[val_1] = val_2

val_1 = int(data[-1])
for i in range(max(cups.keys()) + 1, 1000000 + 1):
    cups[val_1] = i
    val_1 = i
cups[1000000] = int(data[0])
max_val = 1000000

cup = int(data[0])
for move in range(10000000):
    # print_sequence(cup)
    cup_1 = cups[cup]
    cup_2 = cups[cup_1]
    cup_3 = cups[cup_2]
    destination_cup = cup - 1
    while destination_cup in (cup_1, cup_2, cup_3, 0):
        if destination_cup == 0:
            destination_cup = max_val
        else:
            destination_cup -= 1
    cups[cup] = cups[cup_3]
    cups[cup_3] = cups[destination_cup]
    cups[destination_cup] = cup_1
    cup = cups[cup]

final_cup_1 = cups[1]
final_cup_2 = cups[final_cup_1]

print(f'The answer to part 2 = {final_cup_1} x {final_cup_2} = {final_cup_1 * final_cup_2}')