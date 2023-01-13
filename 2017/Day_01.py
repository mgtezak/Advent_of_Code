path = 'Advent_of_Code/2017/puzzle_input/01.txt'

with open(path) as input:
    nums = list(map(int, input.read()))

part1 = sum(int(val) for i, val in enumerate(nums) if val == nums[i-1])

half = int(len(nums) / 2)
part2 = sum(2 * int(a) for a, b in zip(nums[:half], nums[half:]) if a == b)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')