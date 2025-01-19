def part1(puzzle_input):
    grid = puzzle_input.splitlines()
    m = len(grid)
    n = len(grid[0])
    infected = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#':
                infected.add((i, j))

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    x = m // 2
    y = n // 2
    d = 0
    total = 0
    for _ in range(10_000):
        if (x, y) in infected:
            d = (d + 1) % 4
            infected.remove((x, y))
        else:
            d = (d - 1) % 4
            infected.add((x, y))
            total += 1

        x += directions[d][0]
        y += directions[d][1]

    return total
