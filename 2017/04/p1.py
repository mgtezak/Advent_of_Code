def part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    return sum(len(set(line)) == len(line) for line in lines)