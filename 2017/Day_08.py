path = 'Advent_of_Code/2017/puzzle_input/08.txt'

with open(path) as input:
    lines = [line.split() for line in input.read().split('\n')]

def check(condition):
    key, comp, amt = condition
    if comp == '==':
        return d[key] == int(amt)
    elif comp == '>=':
        return d[key] >= int(amt)
    elif comp == '<=':
        return d[key] <= int(amt)
    elif comp == '>':
        return d[key] > int(amt)
    elif comp == '<':
        return d[key] < int(amt)
    else:
        return d[key]!= int(amt)

def perform(operation):
    key, sig, amt = operation
    d[key] += int(amt) if sig == 'inc' else -int(amt)

d = dict()
max_value = 0
for line in lines:
    r1, r2, operation, condition = line[0], line[4], line[:3], line[4:]
    for r in (r1, r2):
        if r not in d:
            d[r] = 0
    if check(condition):
        perform(operation)
    if d[r1] > max_value:
        max_value = d[r1]

print(f'Part 1: {max(d.values())}')
print(f'Part 2: {max_value}')