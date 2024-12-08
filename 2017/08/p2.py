from operator import eq, ne, lt, le, gt, ge


def part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]

    ops = {
        '==': eq,
        '!=': ne,
        '<':  lt,
        '<=': le,
        '>':  gt,
        '>=': ge
    }

    def check(condition):
        key, comp, amt = condition
        first, compare, second = d[key], ops[comp], int(amt)
        return compare(first, second)

    def perform(operation):
        key, sig, amt = operation
        d[key] += int(amt) if sig == 'inc' else -int(amt)

    d = dict()
    max_value = 0
    for line in lines:
        r1, r2, operation, condition = line[0], line[4], line[:3], line[4:]
        for r in (r1, r2):
            if r not in d:
                d[r] = 0
        if check(condition):
            perform(operation)
        if d[r1] > max_value:
            max_value = d[r1]

    return max_value
