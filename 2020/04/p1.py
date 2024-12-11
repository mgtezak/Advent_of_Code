def part1(puzzle_input):
    passports = [p.split() for p in puzzle_input.split('\n\n')]
    valid = 0

    for p in passports:
        if len(p) == 8:
            valid += 1
        elif len(p) == 7 and not any(f.startswith('cid') for f in p):
            valid += 1
            
    return valid