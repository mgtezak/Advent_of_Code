from itertools import permutations

with open('Advent_of_Code/2015/puzzle_input/09.txt') as input:
    lines = [line.split() for line in input.read().split('\n')]

locs = {line[0] for line in lines} | {lines[-1][2]}

perms = list(permutations(locs))

# verbose:
distances = {}
for p in perms:
    total_distance = 0
    for i in range(7):
        start = p[i]
        stop = p[i+1]
        dist = [int(line[-1]) for line in lines if start in line and stop in line][0]
        total_distance += dist
    distances[p] = total_distance

# one-liner:
distances = {p: sum([int(line[-1]) for line in lines if p[i] in line and p[i+1] in line][0] for i in range(7)) for p in perms}

one = min(distances.values())
two = max(distances.values())

print(f'Part 1: {one}')
print(f'Part 2: {two}')