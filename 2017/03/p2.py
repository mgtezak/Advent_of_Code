def part2(puzzle_input):
    puzzle_input = int(puzzle_input)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # east, north, west, south
    def get_neighbors(x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                yield x+i, y+j

    x = y = facing = 0      # start at coords (0, 0), facing east, 
    steps = steps_left = 1  # distance between corners. distance from current position to next corner.
    squares = {(0, 0): 1}
    square_val = 1
    while square_val <= puzzle_input:
        i, j = directions[facing]    
        x += i
        y += j
        steps_left -= 1
        if not steps_left:
            facing = (facing + 1) % 4   # turn left by 90 degrees
            if not facing % 2:          # if now facing east or west, increase number of steps to reach next corner
                steps += 1
            steps_left = steps
        square_val = sum(squares.get((i, j), 0) for i, j in get_neighbors(x, y))
        squares[(x, y)] = square_val
    return square_val