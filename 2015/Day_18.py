'''Very slow solution. Should figure out how to do this more efficiently with numpy at some point.'''

from copy import deepcopy

with open('Advent_of_Code/2015/puzzle_input/18.txt') as input:
    lines = input.read().split('\n')

def get_neighbors(x, y):
    return [(x+i, y+j) for i in range(-1,2) for j in range(-1,2) if x+i in range(len(grid)) and y+j in range(len(grid)) and (i,j) != (0,0)]

def get_num_lit_neighbors(x, y, grid):
    return sum([grid[j][i] == 1 for i, j in get_neighbors(x, y)])

def switch(grid, corners_on=False):
    new_grid = deepcopy(grid)
    corners = [(0, 0), (99, 0), (0, 99), (99, 99)]
    for y in range(len(grid)):
        for x in range(len(grid)):
            if (corners_on == True and (x, y) in corners) or (get_num_lit_neighbors(x, y, grid) == 3) or (grid[y][x] == 1 and get_num_lit_neighbors(x, y, grid) == 2):
                new_grid[y][x] = 1
            else:
                new_grid[y][x] = 0
    return new_grid

def switch_n_times(grid, n, corners_on=False):
    for _ in range(n):
        grid = switch(grid, corners_on)
    return grid

def get_grid():
    grid = [[0 for _ in range(100)] for _ in range(100)]
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == '#':
                grid[y][x] = 1
    return grid

grid = get_grid()
grid_2 = deepcopy(grid)

grid = switch_n_times(grid, 100)
grid_2 = switch_n_times(grid_2, 100, corners_on=True)

part1 = sum(val for row in grid for val in row)
part2 = sum(val for row in grid_2 for val in row)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')