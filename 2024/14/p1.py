import re
import math


def part1(puzzle_input, is_example_input=False):
    m = 7 if is_example_input else 103
    n = 11 if is_example_input else 101

    m_half, n_half = m//2, n//2
    quadrants = [0] * 4
    for line in puzzle_input.split('\n'):
        x, y, i, j = map(int, re.findall(r'(-?\d+)', line))
        x = (x + 100*i) % n
        y = (y + 100*j) % m
        if x == n_half or y == m_half:
            continue
        
        idx = (x < n_half) * 2  + (y < m_half)
        quadrants[idx] += 1

    return math.prod(quadrants)
