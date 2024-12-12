def part2(puzzle_input):
    movements = [(m.split()[0], int(m.split()[1])) for m in puzzle_input.split('\n')]
    x = y = aim = 0
    for c, n in movements:
        if c == 'forward':
            x += n
            y += aim * n
        elif c == 'up':
            aim -= n
        elif c == 'down':
            aim += n
    return x * y