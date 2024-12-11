def part1(puzzle_input):
    adapters = sorted(map(int, puzzle_input.split('\n')))
    joltage = 0
    jolt_diff = [3]
    for a in adapters:
        jolt_diff.append(a - joltage)
        joltage = a
    return jolt_diff.count(1) * jolt_diff.count(3)