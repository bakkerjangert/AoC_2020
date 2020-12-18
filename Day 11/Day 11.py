import copy
with open('input.txt') as f:
    lines = f.read().splitlines()


def check_seat(x, y):
    if grid[y][x] == '.':
        return None
    count_hash = 0
    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            if dx == 0 and dy == 0:
                # skip seat to be checked
                continue
            if 0 <= x + dx < x_max:
                if 0 <= y + dy < y_max:
                    if grid[y + dy][x + dx] == '#':
                        count_hash += 1
            if count_hash >= 4 and grid[y][x] == '#':
                return 'L'
            # print(f'for x,y ({x}, {y}) the count is {count_hash}')
    if count_hash == 0 and grid[y][x] == 'L':
        return '#'
    return None


def check_seat_part2(x, y):
    if grid[y][x] == '.':
        return None
    count_hash = 0
    # up
    dx, dy = 0, -1
    while y + dy >= 0:
        if grid[y + dy][x + dx] == '#':
            count_hash += 1
            break
        elif grid[y + dy][x + dx] == 'L':
            break
        else:
            dy -= 1
    # up-right
    dx, dy = 1, -1
    while y + dy >= 0 and x + dx < x_max:
        if grid[y + dy][x + dx] == '#':
            count_hash += 1
            break
        elif grid[y + dy][x + dx] == 'L':
            break
        else:
            dy -= 1
            dx += 1
    # rigth
    dx, dy = 1, 0
    while x + dx < x_max:
        if grid[y + dy][x + dx] == '#':
            count_hash += 1
            break
        elif grid[y + dy][x + dx] == 'L':
            break
        else:
            dx += 1
    # right-down
    dx, dy = 1, 1
    while y + dy < y_max and x + dx < x_max:
        if grid[y + dy][x + dx] == '#':
            count_hash += 1
            break
        elif grid[y + dy][x + dx] == 'L':
            break
        else:
            dy += 1
            dx += 1
    # down
    dx, dy = 0, 1
    while y + dy < y_max:
        if grid[y + dy][x + dx] == '#':
            count_hash += 1
            break
        elif grid[y + dy][x + dx] == 'L':
            break
        else:
            dy += 1
    # down-left
    dx, dy = -1, 1
    while y + dy < y_max and x + dx >= 0:
        if grid[y + dy][x + dx] == '#':
            count_hash += 1
            break
        elif grid[y + dy][x + dx] == 'L':
            break
        else:
            dx -= 1
            dy += 1
    # left
    dx, dy = -1, 0
    while x + dx >= 0:
        if grid[y + dy][x + dx] == '#':
            count_hash += 1
            break
        elif grid[y + dy][x + dx] == 'L':
            break
        else:
            dx -= 1
    # left-up
    dx, dy = -1, -1
    while y + dy >= 0 and x + dx >= 0:
        if grid[y + dy][x + dx] == '#':
            count_hash += 1
            break
        elif grid[y + dy][x + dx] == 'L':
            break
        else:
            dx -= 1
            dy -= 1
    if count_hash >= 5 and grid[y][x] == '#':
        return 'L'
    if count_hash == 0 and grid[y][x] == 'L':
        return '#'
    return None


def print_grid():
    for line in grid:
        for char in line:
            print(char, end='')
        print('')


grid = []

for line in lines:
    grid.append([])
    for char in line:
        grid[-1].append(char)

grid2 = copy.deepcopy(grid)

x_max = len(grid[0])
y_max = len(grid)

while True:
    none_counter = 0
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            val = check_seat(i, j)
            if val is not None:
                new_grid[j][i] = val
            else:
                none_counter += 1
    if none_counter == len(grid) * len(grid[0]):
        break
    grid = copy.deepcopy(new_grid)
    # print(f'\n--- after {iter} iterations ---')
    # print_grid()

answer = 0
for line in grid:
    answer += line.count('#')

print(f'The answer to part 1 = {answer}')

grid = copy.deepcopy(grid2)

while True:
    none_counter = 0
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            val = check_seat_part2(i, j)
            if val is not None:
                new_grid[j][i] = val
            else:
                none_counter += 1
    if none_counter == len(grid) * len(grid[0]):
        break
    grid = copy.deepcopy(new_grid)
    # print(f'\n--- after {iter} iterations ---')
    # print_grid()

answer = 0
for line in grid:
    answer += line.count('#')

print(f'The answer to part 2 = {answer}')