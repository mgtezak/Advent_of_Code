def part1(puzzle_input):
    lines = puzzle_input.splitlines()
    total = 0
    for line in lines:
        first = max(line[:-1])
        second = max(line[line.find(first)+1:])
        total += int(first + second)

    return total
