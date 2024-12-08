def part1(puzzle_input):
    lines = [line for line in puzzle_input.split('\n')]
    msg = ''
    for i in range(len(lines[0])):
        letters = [line[i] for line in lines]
        most_freq = sorted((letters.count(l), l) for l in letters)[-1][1]
        msg += most_freq
    return msg
