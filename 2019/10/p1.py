import math

def part1(puzzle_input):

    asteroids = [(x, y) for y, line in enumerate(puzzle_input.split("\n")) for x, pos in enumerate(line) if pos == '#']

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

    n_visible_asteroids = max((sum(check_visibility(*a, *b) for b in asteroids), a) for a in asteroids)[0]
    return n_visible_asteroids