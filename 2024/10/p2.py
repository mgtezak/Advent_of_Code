from functools import cache


def part2(puzzle_input):

    @cache
    def distinct_paths(r, c):
        if (height := grid[r][c]) == 9:
            return 1
        paths = 0
        if r > 0 and grid[r-1][c] == height + 1:
            paths += distinct_paths(r-1, c)
        if c > 0 and grid[r][c-1] == height + 1:
            paths += distinct_paths(r, c-1)
        if r < m-1 and grid[r+1][c] == height + 1:
            paths += distinct_paths(r+1, c)
        if c < n-1 and grid[r][c+1] == height + 1:
            paths += distinct_paths(r, c+1)
        return paths

    grid = [[int(num) for num in row] for row in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    score = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 0:
                score += distinct_paths(r, c)

    return score
