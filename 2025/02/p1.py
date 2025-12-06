def part1(puzzle_input):
    ranges = [list(map(int, pair.split("-"))) for pair in puzzle_input.split(",")]
    invalid = 0 
    for i in range(1, 100_000):
        candidate = int(str(i) * 2)
        for lower, upper in ranges:
            if lower <= candidate <= upper:
                invalid += candidate
                break

    return invalid
