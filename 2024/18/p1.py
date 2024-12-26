from collections import deque


def part1(puzzle_input, is_example_input=False):
    n = 7 if is_example_input else 71
    bytes = 12 if is_example_input else 1024
    grid = [['.'] * n for _ in range(n)]

    for line in puzzle_input.split('\n')[:bytes]:
        x, y = map(int, line.split(','))
        grid[y][x] = '#'

    def get_valid_neighbors(x, y):
        for i, j in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if (i in range(n) and
                j in range(n) and 
                grid[j][i] == '.' and
                (i, j) not in visited
            ):
                yield i, j

    queue = deque([(0, 0, 0)])
    visited = set()
    distance = 0
    while queue:
        x, y, distance = queue.popleft()
        if x == y == n-1:
            return distance
        
        for i, j in get_valid_neighbors(x, y):
            queue.append((i, j, distance + 1))
            visited.add((i, j)) 
    