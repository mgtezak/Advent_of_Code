def part1(puzzle_input):
    x = y = 0
    directions = {'v': (0, -1), '^': (0, 1), '<': (-1, 0), '>': (1, 0)}
    visited = {(x, y)}
    for move in puzzle_input:
        x += directions[move][0]
        y += directions[move][1]
        visited.add((x, y))
    return len(visited)
