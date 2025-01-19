def part2(puzzle_input):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3

    grid = puzzle_input.splitlines()
    m = len(grid)
    n = len(grid[0])
    status = {}
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#':
                status[(i, j)] = INFECTED

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    x = m // 2
    y = n // 2
    d = 0
    total = 0
    for _ in range(10_000_000):
        s = status.get((x, y), CLEAN)
        if s == CLEAN:
            d = (d - 1) % 4
            status[(x, y)] = WEAKENED
        if s == WEAKENED:
            total += 1
            status[(x, y)] = INFECTED
        elif s == INFECTED:
            d = (d + 1) % 4
            status[(x, y)] = FLAGGED
        elif s == FLAGGED:
            d = (d + 2) % 4
            status[(x, y)] = CLEAN

        x += directions[d][0]
        y += directions[d][1]

    return total
