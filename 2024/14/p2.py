import re
from itertools import count


def part2(puzzle_input):
    m = 103
    n = 101
    robots = [
        [int(x) for x in re.findall(r'(-?\d+)', line)]
        for line in puzzle_input.split('\n')
    ]
    N = len(robots)
    for second in count(1):
        coordinates = set()
        overlap = False
        for r in range(N):
            x, y, i, j = robots[r]
            x = (x + i) % n
            y = (y + j) % m
            robots[r][:2] = [x, y]
            if (x, y) in coordinates:
                overlap = True
            coordinates.add((x, y))

        if not overlap:
            return second
