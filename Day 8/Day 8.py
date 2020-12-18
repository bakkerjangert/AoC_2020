with open('input.txt') as f:
    lines = f.read().splitlines()


def run_program(program):
    accumulater = 0
    program_index = 0
    unique_index = set()
    fixed = False

    while program_index not in unique_index:
        unique_index.add(program_index)
        if program[program_index][0] == 'acc':
            accumulater += program[program_index][1]
            program_index += 1
        elif program[program_index][0] == 'jmp':
            program_index += program[program_index][1]
        elif program[program_index][0] == 'nop':
            program_index += 1
        elif program[program_index][0] == 'end':
            fixed = True
            break
        else:
            print(f'Input not understood; terminate program!')
            exit()
    return (fixed, accumulater)


prog = {}
for i in range(len(lines)):
    prog[i] = (lines[i].split(' ')[0], int(lines[i].split(' ')[1]))

print(f'The answer to part 1 = {run_program(prog)[1]}')

# Part 2
index_end = max(prog.keys()) + 1
prog[index_end] = ('end', 0)

nops = []
jmps = []

for key in prog.keys():
    if prog[key][0] == 'jmp':
        jmps.append(key)
    elif prog[key][0] == 'nop':
        nops.append(key)

while True:
    if len(nops) > 0:
        val1 = nops.pop(0)
        prog[val1] = ('jmp', prog[val1][1])
        result = run_program(prog)
        if result[0]:
            break
        prog[val1] = ('nop', prog[val1][1])
    if len(jmps) > 0:
        val1 = jmps.pop(0)
        prog[val1] = ('nop', prog[val1][1])
        result = run_program(prog)
        if result[0]:
            break
        prog[val1] = ('jmp', prog[val1][1])

print(f'The answer to part 2 = {result[1]}')