from collections import defaultdict
from itertools import combinations 


def part1(puzzle_input):
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
            for r, c in [(a+dr, b+dc), (c-dr, d-dc)]:
                if r in range(m) and c in range(n):
                    antinodes.add((r, c))
         
    return len(antinodes)
