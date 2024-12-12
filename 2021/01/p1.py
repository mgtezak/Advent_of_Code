def part1(puzzle_input):
    measurements = list(map(int, puzzle_input.split('\n')))
    count = 0
    for i, m in enumerate(measurements):
        if i == 0:
            continue
        if m > measurements[i-1]:
            count += 1
    return count
