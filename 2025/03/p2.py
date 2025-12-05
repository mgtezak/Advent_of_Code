def part2(puzzle_input):
    lines = puzzle_input.splitlines()
    total = 0
    for line in lines:
        joltage = ""
        start = 0
        for i in reversed(range(12)):
            value = max(line[start:-i])
            start = line.find(value, start) + 1
            joltage += value

        total += int(joltage)

    return total
