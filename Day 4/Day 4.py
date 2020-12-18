with open('input.txt') as f:
    lines = f.read().splitlines()

def check_passport():
    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False
    if passport['hgt'][-2:] == 'cm':
        if not (150 <= int(passport['hgt'][0:-2]) <= 193):
            return False
    elif passport['hgt'][-2:] == 'in':
        if not (59 <= int(passport['hgt'][0:-2]) <= 76):
            return False
    else:
        return False
    string = '0123456789abcdef'
    if len(passport['hcl']) != 7 or passport['hcl'][0] != '#':
        return False
    for char in passport['hcl'][1:]:
        if char not in string:
            return False
    ecls = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if passport['ecl'] not in ecls:
        return False
    numbers = '0123456789'
    if len(passport['pid']) != 9:
        return False
    for num in passport['pid']:
        if num not in numbers:
            return False
    return True

# Part 1
checks = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')
check = [False, False, False, False, False, False, False, False]
valid_passports = 0

for line in lines:
    if line == '':
        if check[0:-1].count(True) == 7:
            valid_passports += 1
        # New checker for passport
        check = [False, False, False, False, False, False, False, False]
        continue
    data = line.split(' ')
    for val in data:
        index_val = checks.index(val.split(':')[0])
        check[index_val] = True

print(f'There are {valid_passports} valid pasports for part 1')

# Part 2
# Set inital passport with every line as False
false_passport = {'byr': 0,
                  'iyr': 0,
                  'eyr': 0,
                  'hgt': '0cm',
                  'hcl': 'xxxxxx',
                  'ecl': 'xxx',
                  'pid': '00000000a'}

passport = false_passport.copy()
valid_passports = 0

for line in lines:
    if line == '':
        if check_passport():
            valid_passports += 1
        # New false passport
        passport = false_passport.copy()
        continue
    data = line.split(' ')
    for val in data:
        passport[val.split(':')[0]] = val.split(':')[1]

print(f'There are {valid_passports} valid pasports for part 2')
