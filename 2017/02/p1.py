def part1(puzzle_input):
    nums = [[int(num) for num in row.split()] for row in puzzle_input.split('\n')]
    return sum(max(row) - min(row) for row in nums)