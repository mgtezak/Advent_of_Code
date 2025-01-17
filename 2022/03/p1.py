import string


def part1(puzzle_input):
    letters = ' ' + string.ascii_letters
    result = 0
    for line in puzzle_input.split():
        half = int(len(line)/2)
        first = line[:half]
        second = line[half:]
        for l in first:
            if l in second:
                result += letters.index(l)
                break

    return result
