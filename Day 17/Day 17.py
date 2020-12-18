with open('input.txt') as f:
    lines = f.read().splitlines()


def print_grid():
    for z in range(coord_min[2], coord_max[2], 1):
        print(f'---- z-layer {z} ----')
        for y in range(coord_min[1], coord_max[1], 1):
            for x in range(coord_min[0], coord_max[0], 1):
                # print(grid[(x, y, z)])
                if (x, y, z) in grid.keys():
                    print(grid[(x, y, z)], end='')
                else:
                    print('.', end='')
            print('')
        print('')


grid = dict()

x, y, z = 0, 0, 0
coord_min = [0, 0, 0]
coord_max = [len(lines[0]), len(lines), 1]

for line in lines:
    for char in line:
        grid[(x, y, z)] = char
        # print(f'--> {(x, y, z)} --> {grid[(x, y, z)]}')
        x += 1
    x = 0
    y += 1

print_grid()

cycles = 6

for cycle in range(cycles):
    coord_min = [i - 1 for i in coord_min]
    coord_max = [i + 1 for i in coord_max]
    new_grid = grid.copy()
    for x in range(coord_min[0], coord_max[0], 1):
        for y in range(coord_min[1], coord_max[1], 1):
            for z in range(coord_min[2], coord_max[2], 1):
                val = '.'
                if (x, y, z) in grid.keys():
                    val = grid[(x, y, z)]
                count = 0
                for dx in range(-1, 2, 1):
                    for dy in range(-1, 2, 1):
                        for dz in range(-1, 2, 1):
                            if dx == 0 and dy == 0 and dz == 0:
                                # don't count own position
                                continue
                            if (x + dx, y + dy, z + dz) in grid.keys():
                                if grid[(x + dx, y + dy, z + dz)] == '#':
                                    count += 1
                if val == '#':
                    if not 2 <= count <= 3:
                        new_grid[(x, y, z)] = '.'
                elif val == '.':
                    if count == 3:
                        new_grid[(x, y, z)] = '#'
    grid = new_grid.copy()
    # print_grid()

print(f'The answer to part 1 = {list(grid.values()).count("#")}')

grid = dict()

x, y, z, w = 0, 0, 0, 0
coord_min = [0, 0, 0, 0]
coord_max = [len(lines[0]), len(lines), 1, 1]

for line in lines:
    for char in line:
        grid[(x, y, z, w)] = char
        x += 1
    x = 0
    y += 1

for cycle in range(cycles):
    coord_min = [i - 1 for i in coord_min]
    coord_max = [i + 1 for i in coord_max]
    new_grid = grid.copy()
    for x in range(coord_min[0], coord_max[0], 1):
        for y in range(coord_min[1], coord_max[1], 1):
            for z in range(coord_min[2], coord_max[2], 1):
                for w in range(coord_min[3], coord_max[3], 1):
                    val = '.'
                    if (x, y, z, w) in grid.keys():
                        val = grid[(x, y, z, w)]
                    count = 0
                    for dx in range(-1, 2, 1):
                        for dy in range(-1, 2, 1):
                            for dz in range(-1, 2, 1):
                                for dw in range(-1, 2, 1):
                                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                                        # don't count own position
                                        continue
                                    if (x + dx, y + dy, z + dz, w + dw) in grid.keys():
                                        if grid[(x + dx, y + dy, z + dz, w + dw)] == '#':
                                            count += 1
                    if val == '#':
                        if not 2 <= count <= 3:
                            new_grid[(x, y, z, w)] = '.'
                    elif val == '.':
                        if count == 3:
                            new_grid[(x, y, z, w)] = '#'
    grid = new_grid.copy()
    # print_grid()

print(f'The answer to part 2 = {list(grid.values()).count("#")}')
