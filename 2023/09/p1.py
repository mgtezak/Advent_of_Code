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
