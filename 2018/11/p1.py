import numpy as np

def part1(puzzle_input):

    def get_power_level(x, y):
        return ((x + 11) * (y + 1) + int(puzzle_input)) * (x + 11) // 100 % 10 - 5

    grid = np.fromfunction(get_power_level, (300, 300))
    max_power = float('-inf')
    for x in range(298):
        for y in range(298):
            power_level = grid[x:x+3, y:y+3].sum()
            if power_level > max_power:
                X, Y = x + 1, y + 1
                max_power = power_level

    return f'{X},{Y}'