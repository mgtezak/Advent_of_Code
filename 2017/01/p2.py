def part2(puzzle_input):
    nums = list(map(int, puzzle_input))
    half = int(len(nums) / 2)
    return sum(2 * int(a) for a, b in zip(nums[:half], nums[half:]) if a == b)
