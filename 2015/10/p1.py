import re


def part1(puzzle_input):

    def replace(match_obj):
        group = match_obj.group(1)
        return str(len(group)) + group[0]

    pattern = re.compile(r'((\d)\2*)')
    number = puzzle_input
    for _ in range(40):
        number = pattern.sub(replace, number)

    return len(number)
