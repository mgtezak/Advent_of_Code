def part1(puzzle_input):

    directions = {'E': 1, 'N': 1j, 'W': -1, 'S': -1j}
    position = 0j
    facing = 1 + 0j

    for line in puzzle_input.split():
        op, val = line[0], int(line[1:])
        if op in 'LR':
            facing *=  (1j if op == 'L' else -1j) ** (val // 90)
        else:
            position += (facing if op == 'F' else directions[op]) * val

    return int(abs(position.real) + abs(position.imag))