import re
import numpy as np


def part2(puzzle_input):
    regex = r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)"
    operations = re.findall(regex, puzzle_input)
    grid = np.zeros((1000, 1000))
    for op, *coords in operations:
        x0, y0, x1, y1 = map(int, coords)
        if op == 'turn on':
            grid[x0:x1+1, y0:y1+1] += 1
        elif op == 'turn off':
            grid[x0:x1+1, y0:y1+1] = np.maximum(0, grid[x0:x1+1, y0:y1+1] - 1)
        else:
            grid[x0:x1+1, y0:y1+1] += 2
    return int(grid.sum())
