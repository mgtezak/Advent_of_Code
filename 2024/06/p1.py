from itertools import cycle


def part1(puzzle_input):
    grid = puzzle_input.split('\n')
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '^':
                r, c = i, j

    direction = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    d = next(direction)
    visited = set([(r, c)])
    while True:
        new_r = r + d[0]
        new_c = c + d[1]
        if new_r not in range(m) or new_c not in range(n):
            break 
        if grid[new_r][new_c] == '#':
            d = next(direction)
        else:
            r, c = new_r, new_c
            visited.add((r, c))

    return len(visited)
