def part2(puzzle_input):
    
    passports = [p.split() for p in puzzle_input.split('\n\n')]
    valid = 0

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

        valid += 1

    return valid