def part2(puzzle_input):
    instructions = [(i.split()[0], int(i.split()[1])) for i in puzzle_input.split('\n')]

    def run_instructions(ins):
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

        if i == len(ins):
            return accumulator

    def generate_new_instructions():
        for i, (op, arg) in enumerate(instructions):
            if op == 'nop':
                yield instructions[:i] + [('jmp', arg)] + instructions[i+1:]
            elif op == 'jmp':
                yield instructions[:i] + [('nop', arg)] + instructions[i+1:]

    for ins in generate_new_instructions():
        if (result := run_instructions(ins)):
            return result