path = 'Advent_of_Code/2021/puzzle_input/05.txt'
import re

regex = r'(\d+),(\d+) -> (\d+),(\d+)'
with open(path) as input:
    lines = [tuple(map(int, coords)) for coords in re.findall(regex, input.read())]
    horizontal = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if x1 == x2 or y1 == y2]
    diagonal = [line for line in lines if line not in horizontal]

covered = dict()

# Part 1:
for x1, y1, x2, y2 in horizontal:
    for x in range(min(x1, x2), max(x1, x2)+1):
        for y in range(min(y1, y2), max(y1, y2)+1):
            if not covered.get((x, y)):
                covered[(x, y)] = 0
            covered[(x, y)] += 1

overlap1 = len([(x, y) for x, y in covered if covered[(x, y)] > 1])

# Part 2:
for x1, y1, x2, y2 in diagonal:
    if (x1 > x2) == (y1 > y2):
        y = min(y1, y2)
        incr = 1
    else:
        y = max(y1, y2)
        incr = -1
    for x in range(min(x1, x2), max(x1, x2)+1):
        if not covered.get((x, y)):
            covered[(x, y)] = 0
        covered[(x, y)] += 1
        y += incr

overlap2 = len([(x, y) for x, y in covered if covered[(x, y)] > 1])


print(f'Part 1: {overlap1}')
print(f'Part 2: {overlap2}')