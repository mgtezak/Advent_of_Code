def part2(puzzle_input):
    return sum(2 + line.count('\\') + line.count('"') for line in puzzle_input.split())