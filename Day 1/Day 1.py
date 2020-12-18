with open('input.txt') as f:
    lines = f.read().splitlines()

goal = 2020
bigger_half = sorted(list(map(int, lines)))
smaller_half = []

# Approach for loop for 2 numbers
# __________________   __________________
# | Smaller Half i | + | Bigger half j |
# ------------------   ------------------
# Changed from pycharm

while True:
    if bigger_half[0] > goal // 2:
        break
    else:
        smaller_half.append(bigger_half.pop(0))

# Part 1
found = False
for number_1 in smaller_half:
    for number_2 in bigger_half:
        if number_1 + number_2 == goal:
            found = True
            print(f'The answer to part 1 = {number_1 * number_2}')
            break
    if found:
        break

# Part 2
found = False
all_numbers = smaller_half + bigger_half

# Approach for loop for 3 numbers
# __________________   __________________   ______________________
# | Smaller Half i | + | Total number j | + | Total number j + n |
# ------------------   ------------------   ----------------------
# Note: Check if total number i or i + n == smaller half; skip in this case!

for num_1 in smaller_half:
    for j in range(len(all_numbers) - 1):
        for k in range(j, len(all_numbers)):
            num_2, num_3 = all_numbers[j], all_numbers[k]
            if num_1 == num_2 or num_1 == num_3:
                # Double numbers shall not be counted
                continue
            if num_1 + num_2 + num_3 == goal:
                found = True
                print(f'The answer to part 2 = {num_1 * num_2 * num_3}')
                break
        if found:
            break
    if found:
        break
