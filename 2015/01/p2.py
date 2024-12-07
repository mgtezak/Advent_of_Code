def part2(puzzle_input):
    floor = 0
    for i, char in enumerate(puzzle_input):
        floor += 1 if char == '(' else -1
        if floor == -1:
            return i + 1