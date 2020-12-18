import math
with open('input.txt') as f:
    lines = f.read().splitlines()

goal = int(lines[0])
IDs = lines[1].split(',')

minimum = 0
answer = None

for ID in IDs:
    if ID != 'x':
        val_1 = int(ID) - goal % int(ID)
        if val_1 < minimum or minimum == 0:
            minimum = val_1
            answer = val_1 * int(ID)

print(f'The answer to part 1 = {answer}')

data = {}

for i in range(len(IDs)):
    if IDs[i] != 'x':
        data[int(IDs[i])] = int(IDs[i]) - i % int(IDs[i])
        print(int(IDs[i]), data[int(IDs[i])])
print('')

lcm = 1
time = 0
IDs = []
found = []
check = True

for ID in sorted(data.keys()):
    offset = data[ID] % ID
    IDs.append(ID)
    if check:
        print(f'--- Check ID {ID} with offset {offset} ---')
    while time % ID != offset:
        time += lcm
        # print(time)
    found.append(ID)
    # update lcm
    # lcm = int(np.lcm.reduce(IDs))
    lcm = abs(lcm * ID) // math.gcd(lcm, ID)
    if check:
        for val in found:
            print(f'Bus ID {val} has offset of {time % val}')
        print(f'The lcm = {lcm}\n')


print(f'The answer to part 2 = {time}\n')

for val in found:
    print(f'Bus ID {val} has offset of {time % val}')
