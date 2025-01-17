from itertools import combinations


def part1(puzzle_input):
    grid = [[ele for ele in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])

    i = 0
    while i < len(grid):
        if '#' not in grid[i]:
            grid.insert(i, ['.'] * n)
            m += 1
            i += 2
        else:
            i += 1

    j = 0
    while j < len(grid[0]):
        if '#' not in [grid[i][j] for i in range(m)]:
            for i in range(m):
                grid[i].insert(j, '.')
            n += 1
            j += 2
        else:
            j += 1

    galaxies = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == '#']
    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        total += abs(x1-x2) + abs(y1-y2)
    
    return total
