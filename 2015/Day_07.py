with open('Advent_of_Code/2015/puzzle_input/07.txt') as input:
    data = input.read().split('\n')

def solve(part2=False):
    
    def calculate(wire):
        if wire.isnumeric():
            return int(wire)
        if wire not in results:
            ops = instructions[wire]
            if len(ops) == 1:
                val = calculate(ops[0])
            else:
                gate = ops[-2]
                if gate == 'AND':
                    val = calculate(ops[0]) & calculate(ops[2])
                elif gate == 'OR':
                    val = calculate(ops[0]) | calculate(ops[2])
                elif gate == 'NOT':
                    val = ~calculate(ops[1])
                elif gate == 'RSHIFT':
                    val = calculate(ops[0]) >> calculate(ops[2])
                elif gate == 'LSHIFT':
                    val = calculate(ops[0]) << calculate(ops[2])
            results[wire] = val
        return results[wire]
    
    instructions = dict()
    results = dict()
    for line in data:
        (ops, val) = line.split(' -> ')
        instructions[val] = ops.split()

    if part2:
        a = calculate('a')
        results = {'b': a}
        
    return calculate('a')

print(f'Part 1: {solve()}')
print(f'Part 2: {solve(part2=True)}')