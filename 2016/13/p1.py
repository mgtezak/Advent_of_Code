from collections import deque


def part1(puzzle_input, is_example_input=False):
    target = (7,4) if is_example_input else (31, 39)
    favorite_number = int(puzzle_input)

    def is_wall(x, y):
        result = x*x + 3*x + 2*x*y + y + y*y + favorite_number
        return bool(bin(result).count('1') % 2)

    visited = {(1, 1)}
    q = deque([(1, 1, 0)])
    while q:
        x, y, steps = q.popleft()
        if (x, y) == target:
            break
        for i, j in {(x+1, y), (x-1, y), (x, y+1), (x, y-1)} - visited:
            if i < 0 or j < 0 or is_wall(i, j):
                continue
            q.append((i, j, steps+1))
            visited.add((i, j))

    return steps
