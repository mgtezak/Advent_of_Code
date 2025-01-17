def part2(puzzle_input):
    steps = int(puzzle_input) + 1
    pos = num = 0
    for i in range(1, 50_000_000):
        pos = (pos + steps) % i
        if pos == 0:
            num = i

    return num
