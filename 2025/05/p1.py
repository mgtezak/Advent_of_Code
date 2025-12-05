def part1(puzzle_input):
    ranges, ids = puzzle_input.split('\n\n')
    ranges = list(list(map(int, line.split('-'))) for line in ranges.splitlines())
    ids = list(map(int, ids.splitlines()))

    fresh_count = 0
    for i in ids:
        for a, b in ranges:
            if a <= i <= b:
                fresh_count += 1
                break

    return fresh_count
