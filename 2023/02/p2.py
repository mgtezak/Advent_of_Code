import re
import math


def part2(puzzle_input):
    total = 0

    for game in puzzle_input.split('\n'):
        max_number = {'red': 0, 'green': 0, 'blue': 0}
        for n, color in re.findall(r'(\d+) (red|green|blue)', game):
            max_number[color] = max(int(n), max_number[color])

        total += math.prod(max_number.values())

    return total
