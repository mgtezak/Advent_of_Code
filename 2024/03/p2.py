import re

def part2(puzzle_input):
    do = r"do\(\)"
    dont = r"don't\(\)"
    mul = r"mul\((\d+),(\d+)\)"
    total = 0
    disabled = False
    for x in re.finditer(f'{do}|{dont}|{mul}', puzzle_input):
        if re.fullmatch(dont, x.group()):
            disabled = True
        elif re.fullmatch(do, x.group()):
            disabled = False
        elif not disabled:
            total += int(x.group(1)) * int(x.group(2))

    return total
