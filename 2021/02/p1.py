def part1(puzzle_input):
    movements = [(m.split()[0], int(m.split()[1])) for m in puzzle_input.split('\n')]
    x = y = 0
    for c, n in movements:
        if c == 'forward':
            x += n
        elif c == 'up':
            y -= n
        elif c == 'down':
            y += n
    return x * y