def part2(puzzle_input):
    measurements = list(map(int, puzzle_input.split('\n')))
    windows = [sum(measurements[j] for j in (i-2, i-1, i)) for i in range(2, len(measurements))]
    count = 0
    for i, m in enumerate(windows):
        if i == 0:
            continue
        if m > windows[i-1]:
            count += 1
    return count
