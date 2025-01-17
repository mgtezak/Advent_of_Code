import re
import math


def part2(puzzle_input):
    lines = puzzle_input.split('\n')

    gear_regex = r'\*'
    gears = dict()
    for i, line in enumerate(lines):
        for m in re.finditer(gear_regex, line):
            gears[(i, m.start())] = []

    number_regex = r'\d+'
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            for r in range(i-1, i+2):
                for c in range(m.start()-1, m.end()+1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(m.group()))

    gear_ratio_sum = 0
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += math.prod(nums)

    return gear_ratio_sum