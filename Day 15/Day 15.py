start_numbers = [17, 1, 3, 16, 19, 0]

# TEST AREA
# start_numbers = [1, 2, 3]

numbers = {}
turn = 1

while True:
    if len(start_numbers) > 0:
        said_number = start_numbers.pop(0)
    elif said_number in numbers.keys():
        if numbers[said_number][0] != turn - 1:
            said_number = turn - numbers[said_number].pop(0) - 1
        else:
            said_number = 0
    else:
        said_number = 0
    if said_number in numbers.keys():
        numbers[said_number].append(turn)
    else:
        numbers[said_number] = [turn]
    if turn == 2020:
        print(f'Turn {turn} the number is {said_number}')
    if turn == 30000000:
        print(f'Turn {turn} the number is {said_number}')
        break
    # if turn % 100000 == 0:
        print(f'current turn = {turn}')

    turn += 1
