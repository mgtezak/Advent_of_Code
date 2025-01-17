import re


def part1(puzzle_input):
    lines = [list(map(int, re.split('[,-]', line))) for line in puzzle_input.split('\n')]
    return sum(a <= c <= d <= b or c <= a <= b <= d for a, b, c, d in lines)
