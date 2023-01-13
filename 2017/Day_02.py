path = 'Advent_of_Code/2017/puzzle_input/02.txt'

with open(path) as input:
    nums = [[int(num) for num in row.split()] for row in input.read().split('\n')]

part1 = sum(max(row) - min(row) for row in nums)
part2 = int(sum(a / b for row in nums for a in row for b in row if a != b and not a % b))

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')