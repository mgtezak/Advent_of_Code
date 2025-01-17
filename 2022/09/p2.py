import numpy as np


def part2(puzzle_input):
    x = [0] * 10
    y = [0] * 10
    visited = {(0, 0)}
    moves = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    for line in puzzle_input.split('\n'):
        direction, steps = line.split()
        for _ in range(int(steps)):              
            x[0] += moves[direction][0]
            y[0] += moves[direction][1]
            for i in range(9):             # move middle and tail
                if abs(x[i] - x[i+1]) > 1 or abs(y[i] - y[i+1]) > 1:
                    x[i+1] += np.sign(x[i] - x[i+1])
                    y[i+1] += np.sign(y[i] - y[i+1])
                    
            visited.add((x[9], y[9]))  # track tail

    return len(visited)
