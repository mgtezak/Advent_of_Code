from operator import sub, add

def part2(puzzle_input):
    lines = puzzle_input.splitlines()
    operators = {"L": sub, "R": add}
    current_position = 50
    landed_on_zero = 0
    for line in lines:
        op = operators[line[0]]
        steps = int(line[1:])
        full_rotations, steps = divmod(steps, 100)
        new_position = op(current_position, steps)
        passed_or_landed = int(current_position != 0 and not (0 < new_position < 100))
        landed_on_zero += full_rotations + passed_or_landed
        current_position = new_position % 100
        
    return landed_on_zero
