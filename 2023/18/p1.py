import re


def part1(puzzle_input):
    regex = r'(\w) (\d+)'
    directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    x = y = 0
    visited = set([(0, 0)])
    for d, steps in re.findall(regex, puzzle_input):
        dx, dy = directions[d]
        for _ in range(int(steps)):
            x += dx
            y += dy
            visited.add((x, y))
    
    # get top-left corner tile and start depth-first-search from its bottom-right neighbor
    x, y = min(visited)
    queue = [(x+1, y+1)]
    while queue:
        x1, y1 = queue.pop()
        for dx, dy in directions.values():
            x2, y2 = x1+dx, y1+dy
            if (x2, y2) not in visited:
                queue.append((x2, y2))
                visited.add((x2, y2))

    return len(visited)
