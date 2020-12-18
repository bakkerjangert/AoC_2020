with open('input.txt') as f:
    lines = f.read().splitlines()


def drive(slope):
    x, y = 0, 0
    trees = 0
    x_limit = len(lines[0])
    for line in lines:
        if y % slope[1] != 0:
            y += 1
            continue
        if line[x] == '#':
            trees += 1
        x = (x + slope[0]) % x_limit
        y += 1
    return trees


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

trees = drive(slopes[1])
print(f'There are {trees} trees on the way for the slope of part 1')

part_2 = 1

for slope in slopes:
    part_2 *= drive(slope)
    print(f'Slope {slope} meets {drive(slope)} trees')
print(f'The answer to part 2 is {part_2}')
