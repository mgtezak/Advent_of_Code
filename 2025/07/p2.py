from functools import cache

def part2(puzzle_input):
    grid = puzzle_input.splitlines()

    @cache
    def dfs(i, j):
        while grid[i][j] == '.':
            i += 1
            if i == len(grid):
                return 1
        
        return dfs(i, j-1) + dfs(i, j+1)
        
    return dfs(1, grid[0].index('S'))
