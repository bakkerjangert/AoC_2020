import re

inputString = open("input.txt", "r").read().splitlines()

def createRegex(index, rules):
    if rules[index] in ['a', 'b']:
        return rules[index]
    else:
        regexString = "("
        for poss in rules[index].split(" "):
            regexString += poss if poss == "|" else createRegex(poss, rules)
        regexString += ")"
        return regexString

def partOne():
    rules = {x: y.replace("\"", "") for x, y in [line.split(": ") for line in inputString if ":" in line]}
    expression = re.compile(createRegex('0', rules))
    print(createRegex('0', rules))
    print(len([line for line in [x for x in inputString if ":" not in x and len(x) > 0] if expression.fullmatch(line) is not None]))

def partTwo():
    rules = {x: y.replace("\"", "") for x, y in [line.split(": ") for line in inputString if ":" in line]}
    expression42 = re.compile(createRegex('42', rules))
    expression31 = re.compile(createRegex('31', rules))
    valid = 0
    for line in [x for x in inputString if ":" not in x and len(x) > 0]:
        count42, count31 = 0, 0
        while expression42.match(line):
            line = line[len(expression42.search(line).group(0)):]
            count42 += 1
        while expression31.match(line):
            line = line[len(expression31.search(line).group(0)):]
            count31 += 1
        if count42 > count31 > 0 and len(line) == 0: valid += 1
    print(valid)

partOne()
partTwo()