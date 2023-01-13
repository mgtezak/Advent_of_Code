path = 'Advent_of_Code/2017/puzzle_input/05.txt'

with open(path) as input:
    instructions = input.read()

def calc_steps(part2=False):
    lines = [int(line) for line in instructions.split('\n')]
    pos = 0
    steps = 0
    while pos in range(0, len(lines)):
        steps += 1
        move = lines[pos]
        lines[pos] += 1 if lines[pos] < 3 or not part2 else -1 
        pos += move
    return steps

print(f'Part 1: {calc_steps()}')
print(f'Part 2: {calc_steps(part2=True)}')