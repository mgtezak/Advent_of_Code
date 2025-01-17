import re


def part1(puzzle_input):
    total = 0

    for line in puzzle_input.split('\n'):
        digits = re.findall(r'(\d)', line)
        total += int(digits[0] + digits[-1])

    return 
