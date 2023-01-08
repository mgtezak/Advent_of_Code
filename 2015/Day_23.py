with open('Advent_of_Code/2015/puzzle_input/23.txt') as input:
    ins = [line.split() for line in input.read().split('\n')]

def read_instructions(part2: bool=False) -> int:
    '''Cycles through list of instructions until index i is out of bounds. Returns the value for b.'''
    d = {'a': 0, 'b': 0} if not part2 else {'a': 1, 'b': 0}
    i = 0
    while i in range(len(ins)):
        if ins[i][0] == 'hlf':
            d[ins[i][1]] /= 2
        elif ins[i][0] == 'tpl':
            d[ins[i][1]] *= 3
        elif ins[i][0] == 'inc':
            d[ins[i][1]] += 1
        elif ins[i][0] == 'jmp':
            i += int(ins[i][1])
            continue
        elif ins[i][0] == 'jie':
            if d[ins[i][1].strip(',')] % 2 == 0:
                i += int(ins[i][2])
                continue
        elif ins[i][0] == 'jio':
            if d[ins[i][1].strip(',')] == 1:
                i += int(ins[i][2])
                continue
        i += 1
    return d['b']

print(f'Part 1: {read_instructions()}')
print(f'Part 2: {read_instructions(part2=True)}')