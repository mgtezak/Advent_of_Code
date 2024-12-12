import re

def part1(puzzle_input):
    # Parse input
    dots, instructions = puzzle_input.split('\n\n')
    dots = [(int(x), int(y)) for x, y in re.findall(r'(\d+),(\d+)', dots)]

    # Create initial transparent
    width = max(dots)[0] + 1
    height = max(dots, key=lambda x: x[1])[1] + 1
    grid = [[' '] * width for _ in range(height)]
    for x, y in dots:
        grid[y][x] = '#'

    # Folding functions
    def fold_up(idx):
        for x in range(width):
            for y in range(1, height-idx):
                if grid[idx + y][x] == '#':
                    grid[idx - y][x] = '#'
        return grid[:idx][:], height // 2

    def fold_left(idx):
        for x in range(1, width-idx):
            for y in range(height):
                if grid[y][idx + x] == '#':
                    grid[y][idx - x] = '#'
        return [row[:idx] for row in grid], width // 2

    # Execute first folding instruction
    match = re.search(r'(x|y)=(\d+)', instructions.split('\n')[0])
    if match.group(1) == 'x':   # vertical folding line
        grid, width = fold_left(int(match.group(2)))
    else:                       # horizontal folding line
        grid, height = fold_up(int(match.group(2)))

    return sum(sum(ele == '#' for ele in row) for row in grid)