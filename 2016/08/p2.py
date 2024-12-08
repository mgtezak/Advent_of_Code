import numpy as np


def part2(puzzle_input):
    instructions = [line.split() for line in puzzle_input.split('\n')]
    display = np.zeros((6, 50))
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
            for row in range(6):
                lights.append(display[row][col])
            lights = lights[-down:] + lights[:-down]
            for row in range(6):
                display[row][col] = lights[row]

    return '\n'.join(''.join(['#' if element == 1 else ' ' for element in row]) for row in display)
