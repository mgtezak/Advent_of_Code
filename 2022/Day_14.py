path = 'Advent_of_Code/2022/puzzle_input/14.txt'
with open(path) as input:
    lines = [[[int(c) for c in coords.split(',')] for coords in line.split(' -> ')] for line in input.read().split('\n')]

# figuring out the dimensionality
x_max = max(x for line in lines for x, _ in line)
y_max = max(y for line in lines for _, y in line)
grid = [['.' for _ in range(x_max+150)] for _ in range(y_max+2)]

# adding rock
for line in lines:
    for i, (x, y) in enumerate(line):
        grid[y][x] = '#'
        if i > 0:
            for x_ in range(*sorted([x, line[i-1][0]])):
                grid[y][x_] = '#'
            for y_ in range(*sorted([y, line[i-1][1]])):
                grid[y_][x] = '#'

def add_sand():
    x, y = (500, 0)
    while y < len(grid) - 1:
        if grid[y+1][x] == '.':
            x, y = x, y+1
        elif grid[y+1][x-1] == '.':
            x, y = x-1, y+1
        elif grid[y+1][x+1] == '.':
            x, y = x+1, y+1
        else:
            break
    grid[y][x] = 'o'
    return x, y

sand = 0
solution_1 = solution_2 = None
while not solution_2:
    x, y = add_sand()
    if not solution_1 and y == len(grid) - 1:
        solution_1 = sand
    elif (x, y) == (500, 0):
        solution_2 = sand +1
    sand += 1

print(f'Part 1: {solution_1}')
print(f'Part 2: {solution_2}')