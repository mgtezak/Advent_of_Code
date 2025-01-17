from collections import deque
import numpy as np


def part2(puzzle_input):
    grid = [list(row) for row in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    assert m == n and grid[n//2][n//2] == 'S', "The grid needs to be square with S exactly in the middle"

    # After having crossed the border of the first grid, every further border crossing is seperated by n steps (length/width of grid)
    # Therefore, the total number of grids to traverse in any direction is 26_501_365 // n = x_final
    # Assumption: at step 26_501_365 another border crossing is taking place
    # If so, then it follows that the first crossing takes place at 26_501_365 % n = remainder
    x_final, remainder = divmod(26_501_365, n)
    border_crossings = [remainder, remainder + n, remainder + 2*n]

    visited = set()
    queue = deque([(n//2, n//2)])
    total = [0, 0]  # [even, odd]
    Y = []
    for step in range(1, border_crossings[-1]+1):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if (i, j) in visited or grid[i%m][j%n] == '#':
                    continue

                visited.add((i, j))
                queue.append((i, j))
                total[step % 2] += 1

        if step in border_crossings:
            Y.append(total[step % 2])

    X = [0, 1, 2]
    coefficients = np.polyfit(X, Y, deg=2)      # get coefficients for quadratic equation y = a*x^2 + bx + c
    y_final = np.polyval(coefficients, x_final) # using coefficients, get y value at x_final
    return y_final.round().astype(int)
