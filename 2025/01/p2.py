from operator import sub, add

def part2(puzzle_input):
    lines = puzzle_input.splitlines()
    operators = {"L": sub, "R": add}
    current = 50
    landed_on_zero = 0
    for line in lines:
        op = operators[line[0]]
        clicks = int(line[1:])
        full_rotations, clicks = divmod(clicks, 100)
        new = op(current, clicks)
        landed_on_zero += full_rotations + int(current != 0 and not (0 < new < 100))
        current = new % 100
        
    return landed_on_zero
