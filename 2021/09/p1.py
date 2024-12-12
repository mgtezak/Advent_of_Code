def part1(puzzle_input):
    grid = [[int(n) for n in row] for row in puzzle_input.split('\n')]
    x_range = range(len(grid[0]))
    y_range = range(len(grid))

    def get_neighbors(x, y):
        adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i, j in adj:
            if x+i in x_range and y+j in y_range:
                yield x+i, y+j

    risk_level_sum = 0
    for y, row in enumerate(grid):
        for x, height in enumerate(row):
            if all(height < grid[j][i] for i, j in get_neighbors(x, y)):
                risk_level_sum += height + 1
    return risk_level_sum