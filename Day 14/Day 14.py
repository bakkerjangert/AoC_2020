with open('input.txt') as f:
    lines = f.read().splitlines()


def set_mask(string):
    for i in range(len(string)):
        if string[i] != 'X':
            mask[i] = string[i]


def set_mask_2(string):
    for i in range(len(string)):
        if string[i] != '0':
            mask[i] = string[i]

def update_mem(index, val):
    bit_num = bin(val).replace("0b", "")
    bit_num = '0' * (36 - len(bit_num)) + bit_num
    for key in mask.keys():
        bit_num = bit_num[:key] + mask[key] + bit_num[key + 1:]
    mem[index] = int(bit_num, 2)

def update_mem_2(val, num):
    bit_num = bin(val).replace("0b", "")
    bit_num = '0' * (36 - len(bit_num)) + bit_num
    for key in mask.keys():
        bit_num = bit_num[:key] + mask[key] + bit_num[key + 1:]
    adress_list = [bit_num]
    while 'X' in bit_num:
        index_X = bit_num.index('X')
        for i in range(len(adress_list)):
            adress_list[i] = adress_list[i][:index_X] + '0' + adress_list[i][index_X + 1:]
            adress_list.append(adress_list[i][:index_X] + '1' + adress_list[i][index_X + 1:])
        bit_num = bit_num[:index_X] + 'F' + bit_num[index_X + 1:]  # 'F' as in finished position
    for adress in adress_list:
        mem[int(adress, 2)] = num


mem = {}

for line in lines:
    if 'mask' in line:
        mask = {}
        set_mask(line.split(' = ')[1])
    else:
        val_1 = int(line.split('[')[1].split(']')[0])
        val_2 = int(line.split(' = ')[1])
        update_mem(val_1, val_2)

print(f'The answer to part 1 is {sum(mem.values())}')

mem = {}

for line in lines:
    if 'mask' in line:
        mask = {}
        set_mask_2(line.split(' = ')[1])
    else:
        val_1 = int(line.split('[')[1].split(']')[0])
        val_2 = int(line.split(' = ')[1])
        update_mem_2(val_1, val_2)

print(f'The answer to part 2 is {sum(mem.values())}')
