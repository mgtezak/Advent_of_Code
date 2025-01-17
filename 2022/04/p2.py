import re


def part2(puzzle_input):
    lines = [list(map(int, re.split('[,-]', line))) for line in puzzle_input.split('\n')]
    return sum(a <= d and c <= b for a, b, c, d in lines)
