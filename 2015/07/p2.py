from operator import and_, or_, not_, rshift, lshift


def part2(puzzle_input):
    operators = {
        'AND': and_,
        'OR': or_,
        'NOT': not_,
        'RSHIFT': rshift,
        'LSHIFT': lshift
    }
    
    def calculate(wire):
        if wire.isnumeric():
            return int(wire)
        if wire not in results:
            ops = instructions[wire]
            if len(ops) == 1:
                val = calculate(ops[0])
            else:
                gate = ops[-2]
                if gate == 'NOT':
                    val = ~calculate(ops[1])
                else:
                    val = operators[gate](calculate(ops[0]), calculate(ops[2]))
            results[wire] = val
        return results[wire]
    
    instructions = dict()
    results = dict()
    for line in puzzle_input.split('\n'):
        (ops, val) = line.split(' -> ')
        instructions[val] = ops.split()

    a = calculate('a')
    results = {'b': a}
    return calculate('a')