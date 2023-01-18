path = 'Advent_of_Code/2020/puzzle_input/06.txt'

with open(path) as input:
    groups = [g.split('\n') for g in input.read().split('\n\n')]

any_yes_sum = 0 # part 1
all_yes_sum = 0 # part 2

for g in groups:
    # part 1
    any_yes = set(q for p in g for q in p)
    any_yes_sum += len(any_yes)
    # part 2
    all_yes = set(q for q in g[0] if all(q in g[i] for i, _ in enumerate(g)))
    all_yes_sum += len(all_yes)

print(f'Part 1: {any_yes_sum}')
print(f'Part 2: {all_yes_sum}')