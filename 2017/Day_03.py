# my puzzle input:
input = 312051

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # east, north, west, south

# part 1:

def get_shortest_path():
    distance = input - 1        # since we start at 1, we subtract 1 from the destination value
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
    

# part 2:

def get_neighbors(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            yield x+i, y+j

def get_square_val():
    x = y = facing = 0      # start at coords (0, 0), facing east, 
    steps = steps_left = 1  # distance between corners. distance from current position to next corner.
    squares = {(0, 0): 1}
    square_val = 1
    while square_val <= input:
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

print(f'Part 1: {get_shortest_path()}')
print(f'Part 2: {get_square_val()}')