from collections import deque


def part2(puzzle_input):
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
    threshold = 100
    path = sorted(visited, key=visited.get)
    for t2 in range(threshold, len(path)):
        for t1 in range(t2 - threshold):
            x1, y1 = path[t1]
            x2, y2 = path[t2]
            distance = abs(x1-x2) + abs(y1-y2)
            if distance <= 20 and t2 - t1 - distance >= threshold:
                cheats += 1
     
    return cheats
