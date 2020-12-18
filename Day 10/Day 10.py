with open('input.txt') as f:
    lines = f.read().splitlines()

adapters = sorted(map(int, lines))

dif = [0, 0, 0]
jolts = 0

for adapter in adapters:
    dif[adapter - jolts - 1] += 1
    jolts = adapter
# add last +3 difference
dif[2] += 1

print(f'Part 1: dif 1 ({dif[0]}) x dif 3 ({dif[2]}) = {dif[0] * dif[2]}')

adapters.insert(0, 0)
required = []

for i in range(len(adapters) - 1):
    if adapters[i + 1] - adapters[i] == 3:
        required.append((adapters[i], adapters[i + 1]))

required = sorted(list(required))
required.insert(0, (0, 0))
required.append((max(adapters), max(adapters)))


answer = 1

for i in range(len(required) - 1):
    start_index = adapters.index(required[i][1])
    end_index = adapters.index(required[i + 1][0])
    subset = adapters[start_index + 1: end_index]
    # Checked subset; all subsets are either 0, 1, 2 or 3 numbers long, every sequence always +1 difference
    # For 3 numbers, at least 1 needs to be in; otherwise jolts += 4 results in an incorrect sequence
    if len(subset) == 1:
        # (a) --> [None]; [a] --> Len = 2
        answer *= 2
    elif len(subset) == 2:
        # (a, b) --> [None]; [a]; [b]; [a, b] --> Len = 4
        answer *= 4
    elif len(subset) == 3:
        # (a, b, c) --> [a]; [a, b], [a, c], [a, b, c]; [b]; [b, c]; [c] --> Len = 7
        answer *= 7
    start_index = end_index

print(f'The answer to part 2 = {answer}')
