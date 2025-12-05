from operator import sub, add

def part1(puzzle_input):
    lines = puzzle_input.splitlines()
    operators = {"L": sub, "R": add}
    current_position = 50
    landed_on_zero = 0
    for line in lines:
        op = operators[line[0]]
        steps = int(line[1:])
        current_position = op(current_position, steps) % 100
        if current_position == 0:
            landed_on_zero += 1

    return landed_on_zero
