import numpy as np

def part1(puzzle_input):
    grid = np.array(
        [[char == '@' for char in line] for line in puzzle_input.splitlines()], 
        dtype=np.uint8
    )
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
    return int((grid & (neighbors < 4)).sum())
