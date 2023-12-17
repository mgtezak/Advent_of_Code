import re
from collections import defaultdict

with open('Advent_of_Code/2023/puzzle_input/15.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    total = 0
    for step in puzzle_input.split(','):
        current_val = 0
        for char in step:
            current_val += ord(char)
            current_val *= 17
            current_val %= 256
        total += current_val

    return total


def part2(puzzle_input):

    labels = defaultdict(list)
    lenses = defaultdict(list)
    regex = r'(\w+)(=|-)(\d+)?'
    for label, op, focal_len in re.findall(regex, puzzle_input):
        hash = 0
        for char in label:
            hash = (hash + ord(char)) * 17 % 256

        if label in labels[hash]:
            i = labels[hash].index(label)
            if op == '-':
                labels[hash].pop(i)
                lenses[hash].pop(i)
            else:
                lenses[hash][i] = int(focal_len)
        elif op == '=':
            labels[hash].append(label)
            lenses[hash].append(int(focal_len))

    total = 0
    for box, lenses in lenses.items():
        for i, focal_len in enumerate(lenses, start=1):
            total += (box+1) * i * focal_len
        
    return total


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))