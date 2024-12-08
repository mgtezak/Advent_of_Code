from collections import deque

def part2(puzzle_input):
    puzzle_input = int(puzzle_input)

    def is_wall(x, y):
        result = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
        return bool(bin(result).count('1') % 2)

    visited = {(1, 1)}
    q = deque([(1, 1, 50)])
    while q:
        x, y, steps = q.popleft()
        if not steps:
            continue
        for i, j in {(x+1, y), (x-1, y), (x, y+1), (x, y-1)} - visited:
            if i < 0 or j < 0 or is_wall(i, j):
                continue
            q.append((i, j, steps-1))
            visited.add((i, j))

    return len(visited)