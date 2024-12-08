from collections import Counter


def part1(puzzle_input):
    count = Counter(puzzle_input.split(','))
    x = count['s']  + count['se'] - count['n']  - count['nw']
    y = count['ne'] + count['se'] - count['sw'] - count['nw']
    if x * y <= 0:      # different signs: cannot move diagonally
        return abs(x) + abs(y)
    return min(abs(x), abs(y)) + abs(x-y)
