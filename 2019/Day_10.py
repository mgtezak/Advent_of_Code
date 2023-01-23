'''Takes more than a second to run. I suspect it can be done more efficiently somehow.'''

path = 'Advent_of_Code/2019/puzzle_input/10.txt'

import math

with open(path) as input:
    asteroids = [(x, y) for y, line in enumerate(input.readlines()) for x, pos in enumerate(line) if pos == '#']

def check_visibility(x1, y1, x2, y2) -> bool:
    '''Make sure the two asteroids aren't the same. Then check vertically, horizontally, 
    with positive and with negative slope whether or not there's another asteroid in the way'''

    if (x1, y1) == (x2, y2):
        return False

    x_min, x_max, y_min, y_max = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    dx, dy = abs(x2-x1), abs(y2-y1)
    gcd = math.gcd(dx, dy)

    if not dx: # up and down
        for y in range(y_min+1, y_max):
            if (x1, y) in asteroids:
                return False

    elif not dy: # left and right
        for x in range(x_min+1, x_max):
            if (x, y1) in asteroids:
                return False

    elif (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2): # top left and bottom right quadrants (y decreases from top to bottom)
        y = y_min + int(dy/gcd)
        for x in range(x_min+int(dx/gcd), x_max, int(dx/gcd)):
            if (x, y) in asteroids:
                return False
            y += int(dy/gcd)

    else: # top right and bottom left quadrants
        y = y_max - int(dy/gcd)
        for x in range(x_min+int(dx/gcd), x_max, int(dx/gcd)):
            if (x, y) in asteroids:
                return False
            y -= int(dy/gcd)

    return True

# part 1:
n_visible_asteroids, optimal_coords = max((sum(check_visibility(*a, *b) for b in asteroids), a) for a in asteroids)


# part 2:
def get_nth_asteroid(x, y, n) -> int:
    '''Find visible asteroids in all directions and sort them by their angle to the current asteroid. 
    Then concatenate the directions clockwise and return the 200th asteroid'''
    
    x_max = max(x for x, _ in asteroids)
    y_max = max(y for _, y in asteroids)

    up    = [(None, x2, y2) for x2, y2 in asteroids if x2 == x and y2 < y and check_visibility(x, y, x2, y2)]
    down  = [(None, x2, y2) for x2, y2 in asteroids if x2 == x and y2 > y and check_visibility(x, y, x2, y2)]
    right = sorted(((y2-y)/(x2-x), x2, y2) for x2, y2 in asteroids if x2 in range(x+1, x_max+1) and y2 in range(0, y_max+1) and check_visibility(x, y, x2, y2))
    left  = sorted(((y2-y)/(x2-x), x2, y2) for x2, y2 in asteroids if x2 in range(0, x) and y2 in range(0, y_max+1) and check_visibility(x, y, x2, y2))

    clockwise = up + right + down + left
    _, x2, y2 = clockwise[n-1]
    return 100 * x2 + y2

print(f'Part 1: {n_visible_asteroids}')
print(f'Part 2: {get_nth_asteroid(*optimal_coords, n=200)}')