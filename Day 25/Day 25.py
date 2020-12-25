with open('input.txt') as f:
    lines = f.read().splitlines()

card_public_key, card_subject = int(lines[0]), 7
door_public_key, door_subject = int(lines[1]), 7
divider = 20201227

# card_public_key = 5764801
# door_public_key = 17807724


def calc_key(sub_num):
    val = 1
    while True:
        yield val
        val = (val * sub_num) % divider


loop = 0
door_check, card_check = False, False
for answer in calc_key(7):
    if answer == door_public_key:
        door_loop = loop
        print(f'door loop = {door_loop}')
        door_check = True
    if answer == card_public_key:
        card_loop = loop
        print(f'card loop = {card_loop}')
        card_check = True
    loop += 1
    if card_check and door_check:
        break

val = 1
for i in range(door_loop):
    val = (val * card_public_key) % divider
print(f'methode 1 = {val}')

val = 1
for i in range(card_loop):
    val = (val * door_public_key) % divider
print(f'methode 2 = {val}')