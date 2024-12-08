import re


def part1(puzzle_input):
    x, y = map(int, re.findall(r'(\d+)', puzzle_input))
    row = col = i = 1
    while (row, col) != (x, y):
        if row > 1:
            row -= 1
            col += 1
        else:
            row = col + 1
            col = 1
        i += 1
    
    code = 20151125
    for _ in range(i-1):
        code = code * 252533 % 33554393

    return code