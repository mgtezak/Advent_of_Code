def part1(puzzle_input):
    instructions = puzzle_input.split(', ')
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # North, East, South, West
    x = y = d = 0   # starting out at (0, 0) facing north
    visited = set()
    for ins in instructions:
        turn, dist = ins[0], int(ins[1:])
        if turn == 'R':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
            
        i, j = directions[d]
        for _ in range(dist):
            x += i
            y += j
            visited.add((x, y))

    return abs(x) + abs(y)