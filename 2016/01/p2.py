def part2(puzzle_input):
    instructions = puzzle_input.split(', ')

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # North, East, South, West

    x = y = d = 0   # starting out at (0, 0) facing north
    visited = set()
    visited_twice = None 

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
            if not visited_twice and (x, y) in visited:
                visited_twice = abs(x) + abs(y)
            visited.add((x, y))

    return visited_twice