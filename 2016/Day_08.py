import numpy as np

with open('Advent_of_Code/2016/puzzle_input/08.txt') as input:
    instructions = [line.split() for line in input.read().split('\n')]


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

n_lit = int(display.sum())

def show_display():
    formatted = ''
    for row in display:
        row = ['#' if element == 1 else ' ' for element in row]
        formatted += '\n' + ''.join(row)
    return formatted

print(f'Part 1: {n_lit}')
print(f'Part 2: {show_display()}')