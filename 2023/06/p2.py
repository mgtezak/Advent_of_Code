import re
import math


def part2(puzzle_input):
    time, distance = puzzle_input.split('\n')
    time = int(''.join(re.findall('\d+', time)))
    distance = int(''.join(re.findall('\d+', distance)))
    exact_acceleration = (time - math.sqrt((time**2 - 4*distance))) / 2
    min_acceleration = int(exact_acceleration + 1)
    return time - 2*min_acceleration + 1
