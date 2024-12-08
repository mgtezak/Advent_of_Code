from operator import eq, ne, lt, le, gt, ge


def part1(puzzle_input):
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
    for line in lines:
        r1, r2, operation, condition = line[0], line[4], line[:3], line[4:]
        for r in (r1, r2):
            if r not in d:
                d[r] = 0
        if check(condition):
            perform(operation)

    return max(d.values())
