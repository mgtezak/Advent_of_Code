import re
import math


with open('Advent_of_Code/2023/puzzle_input/02.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    possible = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    for id, game in enumerate(puzzle_input.split('\n'), start=1):
        for n, color in re.findall(r'(\d+) (red|green|blue)', game):
            if possible[color] < int(n):
                break
        else:
            total += id

    return total



def part2(puzzle_input):
    total = 0
    for game in puzzle_input.split('\n'):
        max_number = {'red': 0, 'green': 0, 'blue': 0}
        for n, color in re.findall(r'(\d+) (red|green|blue)', game):
            max_number[color] = max(int(n), max_number[color])

        total += math.prod(max_number.values())

    return total



print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))