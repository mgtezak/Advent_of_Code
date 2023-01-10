import re

with open('Advent_of_Code/2022/puzzle_input/04.txt') as input:
    lines = [list(map(int, re.split('[,-]', line))) for line in input.read().split('\n')]

contained = sum(1 for a, b, c, d in lines if a <= c <= d <= b or c <= a <= b <= d)
overlapping = sum(1 for a, b, c, d in lines if a <= d and c <= b)

print(f'Part 1: {contained}')
print(f'Part 2: {overlapping}')