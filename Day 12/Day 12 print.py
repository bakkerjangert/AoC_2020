with open('input.txt') as f:
    lines = f.read().splitlines()


def move(direction, steps):
    if direction == 'N':
        pos[0] += steps
    elif direction == 'S':
        pos[0] -= steps
    elif direction == 'E':
        pos[1] += steps
    elif direction == 'W':
        pos[1] -= steps
    else:
        print('Input error, stop the code')
        exit()
    return None


def move_wp(direction, steps):
    if direction == 'N':
        rel_way_pos[0] += steps
    elif direction == 'S':
        rel_way_pos[0] -= steps
    elif direction == 'E':
        rel_way_pos[1] += steps
    elif direction == 'W':
        rel_way_pos[1] -= steps
    else:
        print('Input error, stop the code')
        exit()
    return None


def move_ship(steps):
    pos[0] += rel_way_pos[0] * steps
    pos[1] += rel_way_pos[1] * steps
    return None


directions = ['N', 'E', 'S', 'W']

pos = [0, 0]
ship_directon = 'E'

for line in lines:
    if line[0] == 'R':
        start_index = directions.index(ship_directon)
        index_shift = int(line[1:]) // 90
        ship_directon = directions[(start_index + index_shift) % len(directions)]
    elif line[0] == 'L':
        start_index = directions.index(ship_directon)
        index_shift = int(line[1:]) // 90
        ship_directon = directions[start_index - index_shift]
    elif line[0] == 'F':
        move(ship_directon, int(line[1:]))
    else:
        move(line[0], int(line[1:]))

man_dis = abs(pos[0]) + abs(pos[1])

print(f'The manhattan distance = {man_dis}')

exit()

pos = [0, 0]
rel_way_pos = [1, 10]
print(f'Ship pos = {pos}, relative wp pos = {rel_way_pos}')

for line in lines:
    print(f'Instruction ---> {line}')
    if line[0] == 'R' or line[0] == 'L':
        shift = int(line[1:]) // 90
        if line[0] == 'L':
            shift = -shift + 4
        # Rotate waypoint
        if shift == 1:
            rel_way_pos.reverse()
            rel_way_pos[0] *= -1
        elif shift == 2:
            rel_way_pos[0] *= -1
            rel_way_pos[1] *= -1
        elif shift == 3:
            rel_way_pos.reverse()
            rel_way_pos[1] *= -1
    elif line[0] == 'F':
        move_ship(int(line[1:]))
    else:
        move_wp(line[0], int(line[1:]))
    print(f'Ship pos = {pos}, relative wp pos = {rel_way_pos}\n')

man_dis = abs(pos[0]) + abs(pos[1])

print(f'The manhattan distance = {man_dis}')