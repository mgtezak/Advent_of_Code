def part2(puzzle_input):

    busses, offset = [], []
    for i, b in enumerate(puzzle_input.split()[1].split(',')):
        if b == 'x':
            continue
        busses.append(int(b))
        offset.append(i)

    t, step = 0, busses[0]
    for i in range(1, len(busses)):
        while (t + offset[i]) % busses[i] != 0:
            t += step
        step *= busses[i]

    return t