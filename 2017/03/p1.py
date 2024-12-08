def part1(puzzle_input):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # east, north, west, south
    distance = int(puzzle_input) - 1        # since we start at 1, we subtract 1 from the destination value
    x = y = facing = 0          # start at coords (0, 0), facing east, 
    steps = 1                   # distance between current and next corner
    while distance:
        steps = min(steps, distance)
        i, j = directions[facing]    
        x += i * steps
        y += j * steps
        distance -= steps
        facing = (facing + 1) % 4   # turn left by 90 degrees
        if not facing % 2:          # if now facing east or west, increase number of steps to reach next corner
            steps += 1
    return abs(x) + abs(y)