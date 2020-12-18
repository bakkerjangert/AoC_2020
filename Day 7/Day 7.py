import copy
with open('input.txt') as f:
    lines = f.read().splitlines()

bags = {}

for line in lines:
    bag_1 = line.split(' bags')[0]
    string = line.split('contain ')[1]
    string = string.replace('bags', 'bag')
    string = string.replace('.', ',')
    string += ' '
    string = string.split(' bag, ')
    del string[-1]
    in_bag = []
    nums = []
    for bag in string:
        if bag[0] in '0123456789':
            in_bag.append(bag.split(' ')[1] + ' ' + bag.split(' ')[2])
            nums.append(int(bag.split(' ')[0]))
        else:
            in_bag.append(bag)
            nums.append(0)
    bags[bag_1] = (nums, in_bag)

# Part 1
search = ['shiny gold']
uniques = set()

while len(search) != 0:
    goal = search.pop(0)
    if goal not in uniques:
        uniques.add(goal)
        for bag in bags.keys():
            if goal in bags[bag][1]:
                search.append(bag)
    else:
        pass

answer = len(uniques) - 1  # Shiny gold is also part of uniques!
print(f'A total of {answer} bags hold at least one "Shiny Gold" bag')

# Part 2
goal = 'shiny gold'

goal_seek = list()
goal_seek.append(list(copy.deepcopy(bags[goal])))
goal_seek[-1].append([])
for i in range(len(goal_seek[-1])):
    goal_seek[-1][2].append(False)

# print(goal_seek)

reeksen = []
prev_bag = goal

while len(goal_seek) > 0:
    # print(goal_seek[-1])
    cur_bag = goal_seek[-1][1][0]
    # print(f'bag = {cur_bag}, contains {bags[cur_bag]}')
    if bags[cur_bag][0][0] == 0 and not goal_seek[-1][2][0]:
        # end of line
        reeksen.append([])
        for item in goal_seek:
            reeksen[-1].append((item[0][0], item[1][0]))
        goal_seek[-1][2][0] = True
        # print(reeksen[-1])
    elif goal_seek[-1][2][0]:
        del goal_seek[-1][0][0]
        del goal_seek[-1][1][0]
        del goal_seek[-1][2][0]
        if len(goal_seek[-1][0]) == 0:
            del goal_seek[-1]
    else:
        goal_seek[-1][2][0] = True
        goal_seek.append(list(copy.deepcopy(bags[cur_bag])))
        goal_seek[-1].append([])
        for i in range(len(goal_seek[-1][0])):
            goal_seek[-1][2].append(False)
    # print(len(goal_seek))

answer = 0
for i in range(len(reeksen)):
    val_1 = 1  # Multiplyer
    val_2 = 1
    val_1b = 0  # Actual bags
    val_2b = 0
    overlap = 0
    apply_2 = False
    if reeksen[i] != reeksen[-1]:
        for j in range(len(reeksen[i])):
            if reeksen[i][j] == reeksen[i+1][j]:
                overlap += 1
                apply_2 = True
            else:
                break
    for k in range(len(reeksen[i])):
        val_1 *= reeksen[i][k][0]
        val_1b += val_1
        if k < overlap:
            val_2 *= reeksen[i][k][0]
            val_2b += val_2
    answer += val_1b
    if apply_2:
        answer -= val_2b
    # print('----------')
    # print(f'Reeks 1 = {reeksen[i]}')
    # print(f'Reeks 2 = {reeksen[i + 1]}')
    # print(f'Val 1 = {val_1}, val 2 = {val_2}')

print(f'the answer to part 2 = {answer}')

