path = 'Advent_of_Code/2020/puzzle_input/10.txt'

with open(path) as input:
    adapters = sorted(map(int, input.read().split('\n')))

# part 1:

joltage = 0
jolt_diff = [3]
for a in adapters:
    jolt_diff.append(a - joltage)
    joltage = a

part1 = jolt_diff.count(1) * jolt_diff.count(3)

# part 2:

n_paths = {0: 1}  # dict which records the number of distinct paths to reach a given joltage using the available adapters
for a in adapters:
    n_paths[a] = n_paths.get(a-1, 0) + n_paths.get(a-2, 0) + n_paths.get(a-3, 0)

part2 = n_paths[max(adapters)]

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')