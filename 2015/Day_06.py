import numpy as np

with open('Advent_of_Code/2015/puzzle_input/06.txt') as input:
    commands = [[line[5:8]] + [int(c) for s in line.split() if ',' in s for c in s.split(',')] for line in input.read().split('\n')]

grid_1 = np.zeros((1000, 1000))
grid_2 = grid_1.copy()

for c in commands:  
    x0, y0, x1, y1 = c[1:]
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            if c[0] == 'on ':
                grid_1[y][x] = 1
                grid_2[y][x] += 1
            elif c[0] == 'off':
                grid_1[y][x] = 0
                grid_2[y][x] -= 1 if grid_2[y][x] > 0 else 0
            else:
                grid_1[y][x] = 1 - grid_1[y][x]
                grid_2[y][x]+= 2
        
n_lights_on = int(np.sum(grid_1))
total_brightness = int(np.sum(grid_2))

print(f'Part 1: {n_lights_on}')
print(f'Part 2: {total_brightness}')