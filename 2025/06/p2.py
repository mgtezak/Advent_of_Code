from math import prod

def part2(puzzle_input):
    lines = puzzle_input.splitlines()
    operators = {"*": prod, "+": sum}
    total = 0
    nums = []
    for i in reversed(range(len(lines[0]))):
        column = ''.join(line[i] for line in lines)
        if not column.strip():
            continue

        nums.append(int(column[:-1]))
        if op := operators.get(column[-1]):
            total += op(nums)
            nums = []

    return total
