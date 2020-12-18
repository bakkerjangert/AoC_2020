with open('input.txt') as f:
    lines = f.read().splitlines()


def get_num(string, num):
    minimum = 0
    maximum = num
    for char in string:
        if char == 'F' or char == 'L':
            maximum = maximum - (maximum - minimum + 1) // 2
        if char == 'B' or char == 'R':
            minimum = minimum + (maximum - minimum + 1) // 2
    if maximum != minimum:
        print(f'Error in calculation')
        return None
    return maximum


# Test
# test_1 = 'BFFFBBFRRR'  # row 70, column 7, seat ID 567.
# test_2 = 'FFFBBBFRRR'  # row 14, column 7, seat ID 119.
# test_3 = 'BBFFBBFRLL'  # row 102, column 4, seat ID 820.
#
# print(f'Test 1 = row {get_num(test_1[0:7], 127)}, col {get_num(test_1[7:], 7)}')
# print(f'Test 2 = row {get_num(test_2[0:7], 127)}, col {get_num(test_2[7:], 7)}')
# print(f'Test 3 = row {get_num(test_3[0:7], 127)}, col {get_num(test_3[7:], 7)}')

highest_ID = 0
seats = {}
for i in range(8):
    seats[i] = []

for line in lines:
    row = get_num(line[0:7], 127)
    seat = get_num(line[7:], 7)
    ID = row * 8 + seat
    if ID > highest_ID:
        highest_ID = ID
    seats[seat].append(row)

print(f'The highest ID = {highest_ID}')

found = False
for i in range(8):
    if found:
        break
    ordered_rows = sorted(seats[i])
    for j in range(len(ordered_rows) - 1):
        if ordered_rows[j] != ordered_rows[j + 1] - 1:
            found = True
            my_ID = (ordered_rows[j] + 1) * 8 + i
            break

print(f'My seat ID = {my_ID}')
