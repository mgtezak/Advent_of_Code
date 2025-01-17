import re


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
