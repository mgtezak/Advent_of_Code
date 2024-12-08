def part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    lines = [[''.join(sorted(word)) for word in line] for line in lines]
    return sum(len(set(line)) == len(line) for line in lines)