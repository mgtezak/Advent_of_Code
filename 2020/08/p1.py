def part1(puzzle_input):
    ins = [(i.split()[0], int(i.split()[1])) for i in puzzle_input.split('\n')]
    accumulator = 0
    unvisited = [i for i in range(len(ins))]
    i = 0
    while i in unvisited:
        unvisited.remove(i)
        op, arg = ins[i]
        if op == 'acc':
            accumulator += arg
        if op == 'jmp':
            i += arg
        else:
            i += 1
    return accumulator