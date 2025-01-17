def part1(puzzle_input):
    grid = [list(row) for row in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    for c in range(n):
        lim = 0
        for r in range(m):
            if grid[r][c] == '#':
                lim = r + 1
            elif grid[r][c] == 'O':
                if r > lim:
                    grid[lim][c] = 'O'
                    grid[r][c] = '.'
                lim += 1

    total_load = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 'O':
                total_load += m - r

    return total_load
