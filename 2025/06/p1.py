from math import prod

def part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.splitlines()]
    operators = {"*": prod, "+": sum}
    total = 0
    for i in range(len(lines[0])):
        column = [line[i] for line in lines]
        nums = map(int, column[:-1])
        op = operators[column[-1]]
        total += op(nums)

    return total
