def part1(puzzle_input):
    nums = list(map(int, puzzle_input))
    return sum(int(val) for i, val in enumerate(nums) if val == nums[i-1])
