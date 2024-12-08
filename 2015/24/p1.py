from itertools import combinations
import numpy as np


def part1(puzzle_input):

    data = list(map(int, puzzle_input.split()))
    target = sum(data) // 3
    i = 0
    valid_combs = []
    while not valid_combs: 
        i += 1
        valid_combs = [c for c in combinations(data, i) if sum(c) == target]  

    return min(np.prod(c) for c in valid_combs)