def part2(puzzle_input):
    lines = [int(line) for line in puzzle_input.split('\n')]
    pos = 0
    steps = 0
    while pos in range(0, len(lines)):
        steps += 1
        move = lines[pos]
        lines[pos] += 1 if lines[pos] < 3 else -1 
        pos += move
    return steps