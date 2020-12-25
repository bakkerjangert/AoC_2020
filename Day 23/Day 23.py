from collections import deque
data = list(map(int, '364289715'))
# Testinput
# data = list(map(int, '389125467'))
max_val = max(data)

position = 0

for move in range(100):
    val = data[position]
    # shift val to pos[0]
    data = data[position:] + data[:position]
    sub_set = data[1:4].copy()
    del data[1:4]
    while val not in data[1:]:
        val -= 1
        if val == 0:
            val = max_val
    index_val = data.index(val) + 1
    data[index_val:index_val] = sub_set.copy()
    # shift val back
    data = data[max_val - position:] + data[:max_val - position]
    position += 1
    if position == max_val:
        position = 0
    # print(f'--- Move {move + 1} ---')
    # print(data)

index_1 = data.index(1)
data = data[index_1:] + data[:index_1]
print(f'The answer to part 1 = {"".join(map(str,data[1:]))}')

# Part 2
data = list(map(int, '364289715'))
# Testinput
data = list(map(int, '389125467'))


for i in range(max_val + 1, 1000001):
    data.append(i)
max_val = max(data)

data = deque(data)

position = 0
# print('--- initial position ---')
# print(f'{data[0:10]} ... {data[index_1: index_1 + 10]} ... {data[position: position + 10]}... {data[-10:]}')

for move in range(10000000):
    # Get subset of 3 items after placeholder
    sub_set = []
    for i in range(3):
        sub_set.append(data[position + 1])
        del data[position + 1]
    # Determine new index value
    val = data[position] - 1
    while val not in data:
        val -= 1
        if val == 0:
            val = max_val
    index_val = data.index(val) + 1
    for sub_val in sub_set:
        data.insert(index_val, sub_val)
    position += 1
    if position == max_val:
        position = 0
    if move % 1000 == 0:
        print(f'Move {move} at {move / 10000000 * 100}%')
    # print(f'--- Move {move} ---')
    # print(f'{data[0:10]} ... {data[index_1: index_1 + 10]} ... {data[position: position + 10]}... {data[-10:]}')


index_1 = data.index(1)
answer = data[(index_1 + 1) % len(data)] * data[(index_1 + 2) % len(data)]

print(f'The answer to part 2 = {answer}')