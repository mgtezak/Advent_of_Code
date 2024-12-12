def part1(puzzle_input):
    grid = [[int(n) for n in row] for row in puzzle_input.split()]
    rows, cols = len(grid), len(grid[0])
    flashes = 0
    for _ in range(100):
        flashing = set()
        for r in range(rows):
            for c in range(cols):
                grid[r][c] += 1
                if grid[r][c] >= 10:
                    flashing.add((r, c))
        while flashing:
            r, c = flashing.pop()
            if grid[r][c] == 0:
                continue
            grid[r][c] = 0
            flashes += 1
            for x in range(max(0, r-1), min(rows, r+2)):
                for y in range(max(0, c-1), min(cols, c+2)):
                    if (x == r and y == c) or (grid[x][y] == 0):
                        continue
                    grid[x][y] += 1
                    if grid[x][y] >= 10:
                        flashing.add((x, y))
    return flashes