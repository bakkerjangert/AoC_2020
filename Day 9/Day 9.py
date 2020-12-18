import copy
with open('input.txt') as f:
    lines = f.read().splitlines()


def check_num(num):
    for i in range(len(numbers) - 1):
        if numbers[i] > num:
            continue
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == num:
                return True
    return False


total_numbers = list()

for line in lines:
    total_numbers.append(int(line))

print(total_numbers)

length = 25
numbers = copy.copy(total_numbers[0:length])

for k in range(length, len(total_numbers)):
    val = total_numbers[k]
    if not check_num(val):
        # Numer found
        break
    numbers.pop(0)
    numbers.append(val)

print(f'The answer to part 1 = {val}')

check_list = []
found = False
iteration_1 = 0

for i in range(len(total_numbers) - 1):
    if found:
        break
    check_list = [total_numbers[i]]
    for j in range(i + 1, len(total_numbers)):
        iteration_1 += 1
        check_list.append(total_numbers[j])
        if sum(check_list) == val:
            # Series found
            found = True
            break
        elif sum(check_list) > val:
            # Sum exceeds val
            break
        else:
            continue

check_list.sort()

print(f'The answer to part 2 = {check_list[0] + check_list[-1]} after {iteration_1} iterations')

# Optimisation where a window search over total numbers is done:
# x x x [x x x x] x x x x
# x x x [x x x x x] x x x
# x x x [x x x x x x] x x
# x x x x [x x x x x] x x
# ---------------------->
# If check is to high remove a number (left part + 1)
# If check is to low ad a number (right part + 1)

start_index = 0
end_index = 1
iteration_2 = 0

while True:
    iteration_2 += 1
    check_val = sum(total_numbers[start_index:end_index])
    if check_val < val:
        end_index += 1
    elif check_val > val:
        start_index += 1
    elif check_val == val:
        break

window = total_numbers[start_index:end_index]
print(f'The answer to part 2 = {min(window) + max(window)} after {iteration_2} iterations')

print(window)



