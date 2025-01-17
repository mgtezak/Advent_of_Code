import numpy as np


def part2(puzzle_input):

    def get_smudge_row(grid):
        n_rows = grid.shape[0]
        for r in range(1, n_rows):
            span = min(r, n_rows-r)
            top = grid[r-span : r][::-1]
            bottom = grid[r : r+span]
            if (top != bottom).sum() == 1:
                return r
        return None
    
    def get_smudge_col(grid):
        n_cols = grid.shape[1]
        for c in range(1, n_cols):
            span = min(c, n_cols-c)
            left = grid[:, c-span:c][:, ::-1]
            right = grid[:, c:c+span]
            if (left != right).sum() == 1:
                return c
        return None

    grids = puzzle_input.split('\n\n')
    total = 0
    for grid in grids:
        grid = np.array([list(row) for row in grid.split('\n')])
        if (r := get_smudge_row(grid)) is not None:
            total += r * 100
        else:
            total += get_smudge_col(grid)

    return total
