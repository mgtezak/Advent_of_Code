from collections import deque


def part1(puzzle_input):
    grid = puzzle_input.split('\n')
    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 'S':
                S = (row, col)
            elif grid[row][col] == 'E':
                E = (row, col)

    queue = deque([(*S, 0, dict())])
    while queue:
        x, y, time, visited = queue.popleft()
        visited[(x, y)] = time

        if (x, y) == E:
            break

        for i, j in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if (i in range(m) and
                j in range(n) and
                (i, j) not in visited and
                grid[i][j] != '#'
            ):
                queue.append((i, j, time + 1, visited.copy()))

    cheats = 0
    for (x, y), t1 in visited.items():
        for i, j in [(x+2, y), (x-2, y), (x, y-2), (x, y+2)]:
            if visited.get((i, j), 0) - t1 >= 102:
                cheats += 1
                
    return cheats
