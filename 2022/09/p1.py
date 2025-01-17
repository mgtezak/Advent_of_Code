import numpy as np


def part1(puzzle_input):
    x = [0] * 2
    y = [0] * 2
    visited = {(0, 0)}
    moves = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    for line in puzzle_input.split('\n'):
        direction, steps = line.split()
        for _ in range(int(steps)):              
            x[0] += moves[direction][0]
            y[0] += moves[direction][1]
            if abs(x[0] - x[0+1]) > 1 or abs(y[0] - y[1]) > 1:
                x[1] += np.sign(x[0] - x[1])
                y[1] += np.sign(y[0] - y[1])
                
            visited.add((x[1], y[1])) 

    return len(visited)
