import re


def part1(puzzle_input):
    layers = [(int(l), int(r)) for l, r in re.findall(r'(\d+): (\d+)', puzzle_input)]

    total = 0
    for l, r in layers:
        if l % ((r - 1) * 2) == 0:
            total += l * r

    return total
