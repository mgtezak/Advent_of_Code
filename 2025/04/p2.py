import numpy as np

def part2(puzzle_input):
    grid = np.array(
        [[char == '@' for char in line] for line in puzzle_input.splitlines()], 
        dtype=np.uint8
    )

    def is_removable(grid):
        padded = np.pad(grid, 1)
        neighbors = (
            padded[:-2, :-2] +  # up-left
            padded[:-2, 1:-1] + # up
            padded[:-2, 2:] +   # up-right
            padded[1:-1, :-2] + # left
            padded[1:-1, 2:] +  # right
            padded[2:, :-2] +   # down-left
            padded[2:, 1:-1] +  # down
            padded[2:, 2:]      # down-right
        )
        return grid & (neighbors < 4)
    
    removed = 0
    removable = is_removable(grid)
    while removable.any():
        grid -= removable
        removed += removable.sum()
        removable = is_removable(grid)
    
    return int(removed)