# I took the approach for part 2 (Shoelace Method + Pick's Theorem) from this reddit post:
# https://www.reddit.com/r/adventofcode/comments/18l0qtr/2023_day_18_solutions/?utm_source=share&utm_medium=web2x&context=3
# Shoelace method: https://www.youtube.com/watch?v=FSWPX0XB7a0
# Pick's theorem: https://www.youtube.com/watch?v=uh-yRNqLpOg

import re

with open('Advent_of_Code/2023/puzzle_input/18.txt', 'r') as f:
    puzzle_input = f.read()


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


def part2(puzzle_input):
    regex = r'\(#([a-z0-9]+)([0-3])\)'
    directions = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    x = y = 0
    corners = [(0, 0)]
    boundary_area = 0
    for steps, d in re.findall(regex, puzzle_input):
        steps = int(steps, 16)
        dx, dy = directions[int(d)]
        x += dx * steps
        y += dy * steps
        boundary_area += steps
        corners.append((x, y))

    # Shoelace method
    interior_area = 0
    for i in range(len(corners)-1):
        (x1, y1), (x2, y2) =  corners[i:i+2]
        interior_area += x1*y2 - x2*y1
    interior_area = abs(interior_area) // 2

    # Pick's theorem
    total_area = interior_area + boundary_area//2 + 1

    return total_area


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))