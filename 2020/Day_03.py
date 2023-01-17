path = 'Advent_of_Code/2020/puzzle_input/03.txt'

with open(path) as input:
    slope = input.read().split('\n')

def count_trees(right=3, down=1):
    tree_count = 0
    j = 0
    l = len(slope[0])
    for i, row in enumerate(slope):
        if down == 2 and i%2:
            continue
        if row[j] == '#':
            tree_count += 1
        j = (j + right) % l
    return tree_count

def part2():
    instructions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    mul = 1
    for right, down in instructions:
        mul *= count_trees(right, down)
    return mul

print(f'Part 1: {count_trees()}')
print(f'Part 2: {part2()}')