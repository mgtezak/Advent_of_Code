import re


def part2(puzzle_input):
    regex = re.compile(r'(\d+),(\d+)')
    coords = []
    for line in puzzle_input.split('\n'):
        coords.append([list(map(int, xy)) for xy in regex.findall(line)])

    # figuring out the dimensionality
    x_max = max(x for line in coords for x, _ in line)
    y_max = max(y for line in coords for _, y in line)
    grid = [['.' for _ in range(x_max+150)] for _ in range(y_max+2)]

    # adding rock
    for line in coords:
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
    while True:
        x, y = add_sand()
        if x == 500 and y == 0:
            break
        sand += 1

    return sand + 1
