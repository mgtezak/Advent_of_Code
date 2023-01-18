path = 'Advent_of_Code/2020/puzzle_input/08.txt'

with open(path) as input:
    instructions = [(i.split()[0], int(i.split()[1])) for i in input.read().split('\n')]

def run_instructions(ins=instructions, part2=False):
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

    if not part2 or i == len(ins):
        return accumulator

part1 = run_instructions()


# Part 2:

def generate_new_instructions():
    for i, (op, arg) in enumerate(instructions):
        if op == 'nop':
            yield instructions[:i] + [('jmp', arg)] + instructions[i+1:]
        elif op == 'jmp':
            yield instructions[:i] + [('nop', arg)] + instructions[i+1:]

for ins in generate_new_instructions():
    part2 = run_instructions(ins, part2=True)
    if part2:
        break

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')