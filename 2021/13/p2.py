import re

def part2(puzzle_input):
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
    
    # Execute folding instructions
    for axis, idx in re.findall(r'(x|y)=(\d+)', instructions):
        if axis == 'x':     # vertical line
            grid, width = fold_left(int(idx))
        else:               # horizontal line
            grid, height = fold_up(int(idx))

    return '\n'.join(''.join(row) for row in grid)