with open('Advent_of_Code/2022/puzzle_input/01.txt') as input:
    elves = sorted([sum(map(int, elf.split('\n'))) for elf in input.read().split('\n\n')], reverse=True)

print(f'Part 1: {elves[0]}')
print(f'Part 2: {sum(elves[:3])}')