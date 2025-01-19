# This has helped me so much to understand what's going on:
# https://github.com/dp1/AoC17/blob/master/day23.5.txt

from math import sqrt


def part2(puzzle_input):

    def is_prime(num):
        if num % 2 == 0:
            return False
        upper = int(sqrt(num) + 1) 
        for i in range(3, upper, 2):
            if num % i == 0:
                return False
        return True
    
    first_line = puzzle_input.split('\n')[0]
    b = int(first_line[5:]) * 100 + 100_000
    c = b + 17_000
    h = 0
    for i in range(b, c + 1, 17):
        if not is_prime(i):
            h += 1

    return h
