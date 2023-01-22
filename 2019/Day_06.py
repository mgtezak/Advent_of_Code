path = 'Advent_of_Code/2019/puzzle_input/06.txt'

from collections import defaultdict

with open(path) as input:
    lines = [o.split(')') for o in input.read().split('\n')]

orbits = defaultdict(list)
for x, y in lines:
    orbits[y].append(x)

def get_orbits(y):
    if orbits[y] == ['COM']:
        return ['COM']
    return orbits[y] + [get_orbits(x) for x in orbits[y]][0]

# part 1:
total = sum(len(get_orbits(y)) for y in orbits)

# part 2:
santa = get_orbits('SAN')
me = get_orbits('YOU')
n_steps = len([x for x in santa + me if not (x in santa and x in me)])

print(f'Part 1: {total}')
print(f'Part 2: {n_steps}')