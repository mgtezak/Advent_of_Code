from collections import deque


def part2(puzzle_input, is_example_input=False):
    n = 7 if is_example_input else 71
    bytes = 12 if is_example_input else 1024
    grid = [['.'] * n for _ in range(n)]

    def get_valid_neighbors(x, y, visited):
        for i, j in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if (i in range(n) and
                j in range(n) and 
                grid[j][i] == '.' and
                (i, j) not in visited
            ):
                yield i, j

    def get_path():
        queue = deque([(0, 0, list())])
        visited = set()
        while queue:
            x, y, path = queue.popleft()
            if x == y == n-1:
                return path
            
            for i, j in get_valid_neighbors(x, y, visited):
                queue.append((i, j, path + [(i, j)]))
                visited.add((i, j))

        return None

    path = None
    for i, line in enumerate(puzzle_input.split('\n')):
        x, y = map(int, line.split(','))
        grid[y][x] = '#'
        if i > bytes and (path is None or (x, y) in path):
            path = get_path()
            if path is None:
                return f'{x},{y}'
