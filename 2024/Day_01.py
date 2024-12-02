from collections import defaultdict


with open('Advent_of_Code/2024/puzzle_input/01.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    first = []
    second = []
    for line in puzzle_input.split('\n'):
        a, b = map(int, line.split())
        first.append(a)
        second.append(b)

    distance = 0
    for a, b in zip(sorted(first), sorted(second)):
        distance += abs(a - b)

    return distance


def part2(puzzle_input):
    first = defaultdict(int)
    second = defaultdict(int)
    for line in puzzle_input.split('\n'):
        a, b = map(int, line.split())
        first[a] += 1
        second[b] += 1

    similarity = 0
    for num, count in first.items():
        similarity += num * count * second[num]

    return similarity



print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))