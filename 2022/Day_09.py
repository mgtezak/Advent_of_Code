import numpy as np

with open('Advent_of_Code/2022/puzzle_input/09.txt') as input:
    lines = [line for line in input.read().split('\n')]

def get_visited(knots):
    x = [0 for i in range(knots)]
    y = [0 for i in range(knots)]
    visited = {(0, 0)}
    moves = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    for line in lines:
        direction, steps = line.split()
        for _ in range(int(steps)):                # move head
            x[0] += moves[direction][0]
            y[0] += moves[direction][1]
            for i in range(knots - 1):             # move middle and tail
                if abs(x[i] - x[i+1]) > 1 or abs(y[i] - y[i+1]) > 1:
                    x[i+1] += np.sign(x[i] - x[i+1])
                    y[i+1] += np.sign(y[i] - y[i+1])
            visited.add((x[knots-1], y[knots-1]))  # track tail
    return len(visited)

print(f'Part 1: {get_visited(knots=2)}')
print(f'Part 2: {get_visited(knots=10)}')