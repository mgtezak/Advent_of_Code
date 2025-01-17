def part2(puzzle_input):
    wins_against = {'s': 'r', 'r': 'p', 'p': 's'}
    loses_against = {val: key for key, val in wins_against.items()}
    points = 0
    for line in puzzle_input.split('\n'):
        elf = ['r', 'p', 's'][['A', 'B', 'C'].index(line[0])]
        if line[-1] == 'Y':
            me = elf
            points += 3
        elif line[-1] == 'Z':
            me = wins_against[elf]
            points += 6
        else:
            me = loses_against[elf]

        points += ['r', 'p', 's'].index(me) + 1

    return points
