with open('input.txt') as f:
    lines = f.read().splitlines()

answers = set()
all_answers = []
unique_answers = 0
everyone_answer = 0
people = 0

for line in lines:
    if line == '':
        unique_answers += len(answers)
        for char in answers:
            if all_answers.count(char) == people:
                everyone_answer += 1
        answers = set()
        all_answers = []
        people = 0
        continue
    people += 1
    for char in line:
        answers.add(char)
        all_answers.append(char)

print(f'there are {unique_answers} unique questions answered with yes')
print(f'there are {everyone_answer} questions answered with yes by everyone')