path = 'Advent_of_Code/2020/puzzle_input/04.txt'

with open(path) as input:
    passports = [p.split() for p in input.read().split('\n\n')]

# Part 1:
valid_1 = 0
for p in passports:
    if len(p) == 8:
        valid_1 += 1
    elif len(p) == 7 and not any(f.startswith('cid') for f in p):
        valid_1 += 1

# Part 2:
valid_2 = 0
for p in passports:
    if len(p) < 7:
        continue
    if len(p) == 7 and any(f.startswith('cid') for f in p):
        continue

    fields = {f.split(':')[0]: f.split(':')[1] for f in p}

    if int(fields['byr']) not in range(1920, 2003):
        continue

    if int(fields['iyr']) not in range(2010, 2021):
        continue

    if int(fields['eyr']) not in range(2020, 2031):
        continue
    
    if fields['hgt'][-2:] not in ('cm', 'in'):
        continue
    if fields['hgt'][-2:] == 'cm' and int(fields['hgt'][:-2]) not in range(150, 194):
        continue
    if fields['hgt'][-2:] == 'in' and int(fields['hgt'][:-2]) not in range(59, 77):
        continue

    if not fields['hcl'].startswith('#') or len(fields['hcl']) != 7:
        continue
    if any(char not in '0123456789abcdef' for char in fields['hcl'][1:]):
        continue

    if fields['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        continue
    
    if len(fields['pid']) != 9:
        continue

    valid_2 += 1

print(f'Part 1: {valid_1}')
print(f'Part 2: {valid_2}')