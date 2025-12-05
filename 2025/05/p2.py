def part2(puzzle_input):
    ranges, ids = puzzle_input.split('\n\n')
    ranges = list(list(map(int, line.split('-'))) for line in ranges.splitlines())

    fresh_count = 0
    prev_upper = -1
    for lower, upper in sorted(ranges):
        if upper <= prev_upper:
            continue

        fresh_count += upper - max(lower, prev_upper + 1) + 1
        prev_upper = max(upper, prev_upper)

    return fresh_count
