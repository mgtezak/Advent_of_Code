def part2(puzzle_input):
    lines = [line for line in puzzle_input.split('\n')]
    msg = ''
    for i in range(len(lines[0])):
        letters = [line[i] for line in lines]
        least_freq = sorted((letters.count(l), l) for l in letters)[0][1]
        msg += least_freq
    return msg
