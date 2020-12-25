with open('input.txt') as f:
    lines = f.read().splitlines()


def turn_white_tile(pos):
    count_black = 0
    for tile in adjacent_tiles:
        pos_x = pos[0] + tile[0]
        pos_y = pos[1] + tile[1]
        if (pos_x, pos_y) in tiles.keys():
            # color is black
            count_black += 1
        if count_black > 2:
            return False
    if count_black == 2:
        return True
    else:
        return False


def turn_black_tile(pos):
    count_black = 0
    for tile in adjacent_tiles:
        pos_x = pos[0] + tile[0]
        pos_y = pos[1] + tile[1]
        if (pos_x, pos_y) in tiles.keys():
            # If tile not in dict it is white
            count_black += 1
    if count_black == 0 or count_black > 2:
        return True
    else:
        return False


tiles = dict()

for line in lines:
    pos_x, pos_y = 0, 0
    pos_x += 1 * (line.count('ne') - line.count('nw') + line.count('se') - line.count('sw'))
    pos_y += 2 * (line.count('s') - line.count('n'))
    for char in ('ne', 'se', 'nw', 'sw'):
        line = line.replace(char, '')
    pos_x += 2 * (line.count('e') - line.count('w'))
    if (pos_x, pos_y) in tiles.keys():
        del tiles[(pos_x, pos_y)]
    else:
        tiles[(pos_x, pos_y)] = 'black'

print(f'The answer to part 1 = {len(tiles)}')

adjacent_tiles = ((-1, 2), (1, 2), (-2, 0), (2, 0), (-1, -2), (1, -2))

for day in range(100):
    tiles_copy = tiles.copy()
    checked = set()
    for tile in tiles.keys():
        # Color = black
        if turn_black_tile(tile) and tile not in checked:
            del tiles_copy[tile]
        checked.add(tile)
        for adjacent_tile in adjacent_tiles:
            adjacent_pos = (tile[0] + adjacent_tile[0], tile[1] + adjacent_tile[1])
            if adjacent_pos not in checked:
                if adjacent_pos in tiles.keys():
                    # Color = black
                    if turn_black_tile(adjacent_pos):
                        del tiles_copy[adjacent_pos]
                else:
                    # Color = white
                    if turn_white_tile(adjacent_pos):
                        tiles_copy[adjacent_pos] = 'black'
                checked.add(adjacent_pos)
            else:
                # Tile already checked
                pass
    tiles = tiles_copy.copy()
    print(f'--- Day {day + 1} ---')
    print(f'There are {list(tiles.values()).count("black")} black tiles')

print(f'The answer to part 2 = {list(tiles.values()).count("black")}')