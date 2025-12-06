def part2(puzzle_input):
    ranges = [list(map(int, pair.split("-"))) for pair in puzzle_input.split(",")]
    invalid = set()
    for i in range(1, 100_000):
        for repeat in range(2, 11):
            candidate = int(str(i) * repeat)
            if candidate > 10_000_000_000:
                break
            for lower, upper in ranges:
                if lower <= candidate <= upper:
                    invalid.add(candidate)
                    break

    return sum(invalid)
