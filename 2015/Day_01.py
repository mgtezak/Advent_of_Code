with open('Advent_of_Code/2015/puzzle_input/01.txt') as input:
    data = input.read()

part1 = data.count('(') - data.count(')')

def part2(floor=0):
    for i, char in enumerate(data):
        floor += 1 if char == '(' else -1
        if floor == -1:
            return i + 1

print(f'Part 1: {part1}')
print(f'Part 2: {part2()}')