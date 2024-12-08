import numpy as np


def part1(puzzle_input, is_example_input=False):
    n_rows = 3 if is_example_input else 6
    n_cols = 7 if is_example_input else 50

    instructions = [line.split() for line in puzzle_input.split('\n')]
    display = np.zeros((n_rows, n_cols))

    for i in instructions:
        if i[0] == 'rect':
            cols, rows = int(i[1].split('x')[0]), int(i[1].split('x')[1])
            for x in range(cols):
                for y in range(rows):
                    display[y][x] = 1

        elif i[1] == 'row':
            row_index = int(i[2].strip('y='))
            right = int(i[-1])
            row = list(display[row_index])
            row = row[-right:] + row[:-right]
            display[row_index] = row

        elif i[1] == 'column':
            col = int(i[2].strip('x='))
            down = int(i[-1])
            lights = []
            for row in range(n_rows):
                lights.append(display[row][col])
            lights = lights[-down:] + lights[:-down]
            for row in range(n_rows):
                display[row][col] = lights[row]

    return int(display.sum())
