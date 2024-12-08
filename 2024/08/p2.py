from collections import defaultdict
from itertools import combinations 


def part2(puzzle_input):
    grid = puzzle_input.split()
    locations = defaultdict(set)
    m, n = len(grid), len(grid[0])
    for r in range(m):
        for c in range(n):
            if grid[r][c] != '.':
                locations[grid[r][c]].add((r, c))

    antinodes = set()
    for loc in locations.values():
        for (a, b), (c, d) in combinations(loc, 2):
            dr = a - c
            dc = b - d

            row, col = a, b
            while row in range(m) and col in range(n):
                antinodes.add((row, col))
                row += dr
                col += dc
                
            row, col = c, d
            while row in range(m) and col in range(n):
                antinodes.add((row, col))
                row -= dr
                col -= dc

    return len(antinodes)
