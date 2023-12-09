with open('Advent_of_Code/2023/puzzle_input/09.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    total = 0
    for line in puzzle_input.split('\n'):
        nums = [int(n) for n in line.split()]
        final_nums = []

        while set(nums) != set([0]):
            final_nums.append(nums[-1])
            nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]

        total += sum(final_nums)

    return total


def part2(puzzle_input):
    total = 0
    for line in puzzle_input.split('\n'):
        nums = [int(n) for n in line.split()]
        first_nums = []
        
        while set(nums) != set([0]):
            first_nums.append(nums[0])
            nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]

        for i, num in enumerate(first_nums):
            total += num if i % 2 == 0 else -num

    return total


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))