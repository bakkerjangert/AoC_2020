with open('input.txt') as f:
    lines = f.read().splitlines()

class SubGrid(object):
    def __init__(self, ID, grid):
        self.ID = ID
        self.grid = grid
        self.up = self.grid[0]
        self.down = self.grid[-1]
        self.left = [row[0] for row in self.grid]
        self.right = [row[-1] for row in self.grid]
        self.edges = [self.up, self.up[::-1], self.down, self.down[::-1],
                      self.left, self.left[::-1], self.right, self.right[::-1]]
        self.pos = None
        # Adjacent = up - right - down - left
        self.adjacent = [[], [], [], []]

    def update_edge(self):
        self.left = [row[0] for row in self.grid]
        self.right = [row[-1] for row in self.grid]
        self.up = self.grid[0]
        self.down = self.grid[-1]

    def mirror_x(self):
        for line in self.grid:
            line.reverse()
        self.update_edge()
        self.adjacent[1], self.adjacent[3] = self.adjacent[3], self.adjacent[1]

    def mirror_y(self):
        self.grid.reverse()
        self.update_edge()
        self.adjacent[0], self.adjacent[2] = self.adjacent[2], self.adjacent[0]

    def rotate(self):
        temp = list(zip(*self.grid[::-1]))

        self.grid = list(map(list, temp))
        self.update_edge()
        self.adjacent = self.adjacent[3:] + self.adjacent[:3]


    def print_grid(self):
        print(f'\n--- Printing Grid {self.ID} ---\n')
        print(f'  {"".join(self.up)}')
        print('')
        for i in range(len(self.grid)):
            print(f'{self.left[i]} {"".join(self.grid[i])} {self.right[i]}')
        print('')
        print(f'  {"".join(self.down)}')


grid = []
grids = dict()
first = True
ID = None

for line in lines:
    if line == '':
        continue
    if ':' in line and not first:
        grids[ID] = SubGrid(ID, grid)
    if ':' in line:
        first = False
        ID = int(line.split(' ')[1].split(':')[0])
        grid = []
    else:
        grid.append([])
        for char in line:
            grid[-1].append(char)
grids[ID] = SubGrid(ID, grid)  # Do not forget ot add last grid

grid_IDs = list(grids.keys())
answer = 1
corner_pieces = []
edge_pieces = []
mid_pieces = []
for ID_1 in grid_IDs:
    for ID_2 in grid_IDs:
        if ID_1 == ID_2:
            # Do not check matching itself
            continue
        if grids[ID_1].up in grids[ID_2].edges:
            grids[ID_1].adjacent[0].append(ID_2)
        if grids[ID_1].right in grids[ID_2].edges:
            grids[ID_1].adjacent[1].append(ID_2)
        if grids[ID_1].down in grids[ID_2].edges:
            grids[ID_1].adjacent[2].append(ID_2)
        if grids[ID_1].left in grids[ID_2].edges:
            grids[ID_1].adjacent[3].append(ID_2)
    count = sum([len(x) for x in grids[ID_1].adjacent])
    if count == 2:
        answer *= ID_1
        corner_pieces.append(ID_1)
    elif count == 3:
        edge_pieces.append(ID_1)
    else:
        mid_pieces.append(ID_1)
    # print(f'ID {ID_1} has the following neigbors {grids[ID_1].adjacent}')

print(f'The answer to part 1 = {answer}, there are {len(edge_pieces)} edge pieces and {len(corner_pieces)} corner pieces')

start_piece = grids[corner_pieces[0]]
# start_piece.print_grid()

while not(len(start_piece.adjacent[0]) == 0 and len(start_piece.adjacent[3]) == 0):
    start_piece.rotate()

big_grid = []
for y in range(len(edge_pieces) // 4 + 2):
    big_grid.append([])
    for x in range(len(edge_pieces) // 4 + 2):
        big_grid[-1].append(start_piece)
        if x != len(edge_pieces) // 4 + 1:
            next_piece = grids[start_piece.adjacent[1][0]]
            while True:
                if len(next_piece.adjacent[3]) == 0:
                    next_piece.rotate()
                elif next_piece.adjacent[3][0] != start_piece.ID:
                    next_piece.rotate()
                elif start_piece.right != next_piece.left:
                    next_piece.mirror_y()
                else:
                    break
        elif y == len(edge_pieces) // 4 + 1:
            # Do not look for next piee in new line if y = y_max
            continue
        else:
            # Find next piece for start next line
            next_piece = grids[big_grid[-1][0].adjacent[2][0]]
            while True:
                if len(next_piece.adjacent[0]) == 0:
                    next_piece.rotate()
                elif next_piece.adjacent[0][0] != big_grid[-1][0].ID:
                    next_piece.rotate()
                elif big_grid[-1][0].down != next_piece.up:
                    next_piece.mirror_x()
                else:
                    break
        start_piece = next_piece


big_data = []

dy = len(big_grid[0][0].grid) - 2 - 1

for y in range(len(big_grid)):
    for x in range(len(big_grid[0])):
        sub_grid = big_grid[y][x]
        if x == 0:
            for i in range(len(sub_grid.grid) - 2):
                big_data.append([])
        for y_2 in range(len(sub_grid.grid) - 2):
            big_data[-1 - dy + y_2] += sub_grid.grid[y_2 + 1][1:-1]

count_hash = 0
for line in big_data:
    count_hash += ''.join(line).count('#')

sea_horse = [(18, 0),
             (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1),
             (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]

sea_horse_data = (19, 2, len(sea_horse))

search_grid = SubGrid('MAIN', big_data)
no_of_monsters = 0
i = 0

while no_of_monsters == 0:
    for y in range(len(search_grid.grid) - sea_horse_data[1]):
        for x in range(len(search_grid.grid[0]) - sea_horse_data[0]):
            found = True
            for coord in sea_horse:
                if search_grid.grid[y + coord[1]][x + coord[0]] != '#':
                    found = False
                    break
            if found:
                no_of_monsters += 1
    # First rotate 3 times; then mirror in x; then rotate 3 times; mirror y (so x and y); rot; mirror x (only y left)
    if i == 3:
        search_grid.mirror_x()
    elif i == 7:
        search_grid.mirror_y()
    elif i == 11:
        search_grid.mirror_x()
    else:
        search_grid.rotate()
    i += 1

print(f'No of seamonsters = {no_of_monsters}')

print(f'The answer to port 2 = {count_hash - no_of_monsters * sea_horse_data[2]}')
