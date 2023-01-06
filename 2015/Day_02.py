import numpy as np

with open('Advent_of_Code/2015/puzzle_input/02.txt') as input:
    lines = [list(map(int, line.split('x'))) for line in input.read().split('\n')]

def part1(total_paper=0):
    for line in lines:
        sides = [line[0]*line[1], line[1]*line[2], line[0]*line[2]]
        total_paper += sum(sides) * 2 + min(sides)
    return total_paper

def part2(total_ribbon=0):
    for line in lines:
        edges = [line[0], line[1], line[2]]
        total_ribbon += np.prod(edges)
        edges.remove(max(edges))
        total_ribbon += sum(edges * 2)
    return total_ribbon

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')   