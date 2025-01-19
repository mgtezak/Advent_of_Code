import re
import numpy as np


def part2(puzzle_input):
    N = 18

    def stringify(grid):
        return ''.join(''.join(map(str, row)) for row in grid)

    def gridify(string):
        grid = [[x == '#' for x in row] for row in string.split('/')]
        return np.array(grid, dtype=int)

    def get_all_derivations(pattern):
        grid = gridify(pattern)
        derivations = {stringify(grid)}
        for _ in range(3):
            grid = np.rot90(grid)
            derivations.add(stringify(grid))

        grid = np.fliplr(grid)
        derivations.add(stringify(grid))
        for _ in range(3):
            grid = np.rot90(grid)
            derivations.add(stringify(grid))

        return derivations

    transformations = {}
    for input, output in re.findall(r'([.#/]+) => ([.#/]+)', puzzle_input):
        for pattern in get_all_derivations(input):
            transformations[pattern] = gridify(output)

    grid = gridify('.#./..#/###')
    for _ in range(N):
        size = len(grid)
        if size % 2 == 0:
            new_size = round(size * 1.5)
            new_grid = np.empty((new_size, new_size), dtype=int)
            for i in range(size // 2):
                for j in range(size // 2):
                    square = stringify(grid[2*i:2*i+2, 2*j:2*j+2])
                    new_grid[3*i:3*i+3, 3*j:3*j+3] = transformations[square]
        else:
            new_size = round(size * 4 / 3)
            new_grid = np.empty((new_size, new_size), dtype=int)
            for i in range(size // 3):
                for j in range(size // 3):
                    square = stringify(grid[3*i:3*i+3, 3*j:3*j+3])
                    new_grid[4*i:4*i+4, 4*j:4*j+4] = transformations[square]

        grid = new_grid

    return grid.sum()
