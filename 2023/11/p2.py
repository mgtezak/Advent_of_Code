from itertools import combinations


def part2(puzzle_input):
    grid = [[ele for ele in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])

    empty_rows = [i for i in range(m) if '#' not in grid[i]]
    empty_cols = [j for j in range(n) if all(grid[i][j] == '.' for i in range(m))]
    galaxies = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == '#']
    
    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        add_rows = 999_999 * sum(r in range(x1, x2) for r in empty_rows)
        add_cols = 999_999 * sum(c in range(y1, y2) for c in empty_cols)
        total += x2 - x1 + add_rows + y2 - y1 + add_cols

    return total
