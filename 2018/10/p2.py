import re

def part2(puzzle_input):
    regex = r'position=<\s*(-?\d+),\s+(-?\d+)> velocity=<\s*(-?\d+),\s+(-?\d+)>'
    points = [tuple(map(int, line)) for line in re.findall(regex, puzzle_input)]
    seconds = 0
    while True:
        new_points = [(x+i, y+j, i, j) for x, y, i, j in points]
        if min(new_points) < min(points):
            break
        points = new_points
        seconds += 1
    x_coords = [p[0] for p in points]
    x_min = min(x_coords)
    x_span = abs(max(x_coords) - x_min)
    y_coords = [p[1] for p in points]
    y_min = min(y_coords)
    y_span = abs(max(y_coords) - y_min)
    grid = [[' ' for _ in range(x_span+1)] for _ in range(y_span+1)]
    for x, y, *_ in points:
        grid[y-y_min][x-x_min] = '#'
    return seconds