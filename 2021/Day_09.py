path = 'Advent_of_Code/2021/puzzle_input/09.txt'

from math import prod

with open(path) as input:
    grid = [[int(n) for n in row] for row in input.read().split('\n')]
    
x_range = range(len(grid[0]))
y_range = range(len(grid))

def get_neighbors(x, y):
    adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i, j in adj:
        if x+i in x_range and y+j in y_range:
            yield x+i, y+j

# Part 1:

risk_level_sum = 0
for y, row in enumerate(grid):
    for x, height in enumerate(row):
        if all(height < grid[j][i] for i, j in get_neighbors(x, y)):
            risk_level_sum += height + 1

# Part 2:

def add_basin():
    size = 0
    queue = [unvisited.pop()]
    while queue:
        x, y = queue.pop()
        if grid[y][x] == 9:
            continue
        size += 1
        for i, j in get_neighbors(x, y):
            if (i, j) in unvisited:
                unvisited.remove((i, j))
                queue.append((i, j))
    basins.append(size) 

unvisited = [(x, y) for x in x_range for y in y_range]  
basins = []
while unvisited:
    add_basin()

largest_basins_prod = prod(sorted(basins)[-3:]) 

print(f'Part 1: {risk_level_sum}')
print(f'Part 2: {largest_basins_prod}')