def part2(puzzle_input):
    nums = [[int(num) for num in row.split()] for row in puzzle_input.split('\n')]
    return int(sum(a / b for row in nums for a in row for b in row if a != b and not a % b))