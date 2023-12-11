from itertools import combinations

with open('Advent_of_Code/2023/puzzle_input/11.txt', 'r') as f:
    puzzle_input = f.read()


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


def part2(puzzle_input):
    grid = [[ele for ele in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])

    empty_rows = [i for i in range(m) if '#' not in grid[i]]
    empty_cols = [j for j in range(n) if all(grid[i][j]=='.' for i in range(m))]

    galaxies = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == '#']
    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        add_rows = 999_999 * sum(r in range(x1, x2) for r in empty_rows)
        add_cols = 999_999 * sum(c in range(y1, y2) for c in empty_cols)
        total += x2 - x1 + add_rows + y2 - y1 + add_cols

    return total


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))