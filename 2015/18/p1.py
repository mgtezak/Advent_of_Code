def part1(puzzle_input, is_example_input=False):
    steps = 4 if is_example_input else 100
    n = 6 if is_example_input else 100

    def get_neighbors(x, y):
        return [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2) if x+i in range(len(grid)) and y+j in range(len(grid)) and (i, j) != (0,0)]

    def get_num_lit_neighbors(x, y, grid):
        return sum([grid[j][i] == 1 for i, j in get_neighbors(x, y)])

    def switch(grid):
        new_grid = [[0] * n for _ in range(n)]
        for y in range(n):
            for x in range(n):
                if (get_num_lit_neighbors(x, y, grid) == 3) or (grid[y][x] == 1 and get_num_lit_neighbors(x, y, grid) == 2):
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
        return new_grid

    grid = [[0] * n for _ in range(n)]
    for y, line in enumerate(puzzle_input.split('\n')):
        for x, val in enumerate(line):
            if val == '#':
                grid[y][x] = 1

    for _ in range(steps):
        grid = switch(grid)

    return sum(sum(row) for row in grid)