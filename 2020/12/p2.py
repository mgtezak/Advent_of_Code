def part2(puzzle_input):

    directions = {'E': 1, 'N': 1j, 'W': -1, 'S': -1j}
    position = 0j
    waypoint = 10 + 1j
    
    for line in puzzle_input.split():
        op, val = line[0], int(line[1:])
        if op in 'LR':
            waypoint *=  (1j if op == 'L' else -1j) ** (val // 90)
        elif op == 'F':
            position += waypoint * val
        else:
            waypoint += directions[op] * val

    return int(abs(position.real) + abs(position.imag))