with open('input.txt') as f:
    lines = f.read().splitlines()

ingredients = dict()
allergies = dict()
data = []

for line in lines:
    left = line.split(' (')[0].split(' ')
    right = line.split('contains ')[1].split(')')[0].split(', ')
    for ingredient in left:
        ingredients[ingredient] = right.copy()
    for allergie in right:
        if allergie not in allergies.keys():
            allergies[allergie] = [left.copy()]
        else:
            allergies[allergie].append(left.copy())
    data.append([left.copy(), right.copy()])

unique_allergies = dict()
iter = 1
while len(allergies) > 0:
    del_keys = []
    # print(f'iteration {iter}')
    for key in allergies.keys():
        check_line = allergies[key][0].copy()
        for item in check_line:
            for i in range(1, len(allergies[key])):
                if item not in allergies[key][i]:
                    allergies[key][0].remove(item)
                    break
        # print(f'{key} --> {allergies[key][0]}')
        if len(allergies[key][0]) == 1:
            unique_allergies[key] = allergies[key][0][0]
            del_keys.append(key)
        elif len(allergies[key][0]) == 0:
            del allergies[key][0]
    for key in del_keys:
        del allergies[key]
        for lists in allergies.values():
            for sub_list in lists:
                if unique_allergies[key] in sub_list:
                    sub_list.remove(unique_allergies[key])
    iter += 1

conteminated_ingredients = list(unique_allergies.values())

count = 0
for line in data:
    for ingredient in line[0]:
        if ingredient not in conteminated_ingredients:
            count += 1
print(f'The answer to part 1 = {count}')

ordered_list = []
for key in sorted(unique_allergies.keys()):
    ordered_list.append(unique_allergies[key])

answer = ','.join(ordered_list)
print('The answer to part 2:')
print(answer)