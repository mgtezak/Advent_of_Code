from operator import sub, add

def part1(puzzle_input):
    lines = puzzle_input.splitlines()
    operators = {"L": sub, "R": add}
    current = 50
    landed_on_zero = 0
    for line in lines:
        op = operators[line[0]]
        clicks = int(line[1:])
        current = op(current, clicks) % 100
        if current == 0:
            landed_on_zero += 1

    return landed_on_zero
