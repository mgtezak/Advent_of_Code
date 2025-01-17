import string


def part2(puzzle_input):
    letters = ' ' + string.ascii_letters
    result = 0
    lines = puzzle_input.split()
    for i in range(0, len(lines), 3):
        for l in lines[i]:
            if l in lines[i+1] and l in lines[i+2]:
                result += letters.index(l)
                break

    return result
