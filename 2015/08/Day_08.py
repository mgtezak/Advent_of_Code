import ast

with open('Advent_of_Code/2015/puzzle_input/08.txt') as input:
    lines = input.read().split()

part1 = sum(len(line) - len(ast.literal_eval(line)) for line in lines)
part2 = sum(2 + line.count('\\') + line.count('"') for line in lines)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')