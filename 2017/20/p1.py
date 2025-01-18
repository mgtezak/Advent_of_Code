import re
import numpy as np


def part1(puzzle_input):
    nums = re.findall(r'(-?\d+)', puzzle_input)
    particles = np.array(nums, dtype=int).reshape(-1, 9)
    particles[:,3:6] += particles[:,6:] # accelerate once before starting to move
    
    for _ in range(1_000):
        particles[:,:6] += particles[:,3:]

    distances = abs(particles[:,:3]).sum(axis=1)
    return np.argmin(distances)
