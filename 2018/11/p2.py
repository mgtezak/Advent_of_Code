import scipy
import numpy as np

def part2(puzzle_input):

    def get_power_level(x, y):
        return ((x + 11) * (y + 1) + int(puzzle_input)) * (x + 11) // 100 % 10 - 5

    grid = np.fromfunction(get_power_level, (300, 300))
    prev_max = float('-inf')
    for size in range(2, 50):
        kernel = np.ones((size, size))
        conv = scipy.signal.convolve2d(grid, kernel, mode='valid')
        x, y = np.unravel_index(np.argmax(conv), conv.shape)
        if (max_val := conv[x, y]) < prev_max:
            break
        prev_max = max_val
        X, Y, SIZE = x + 1, y + 1, size

    return f'{X},{Y},{SIZE}'