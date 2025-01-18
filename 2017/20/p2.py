import re
import numpy as np
from collections import defaultdict


def part2(puzzle_input):
    nums = re.findall(r'(-?\d+)', puzzle_input)
    particles = np.array(nums, dtype=int).reshape(-1, 9)
    particles[:,3:6] += particles[:,6:] # accelerate once before starting to move

    for _ in range(1000):
        particles[:,:6] += particles[:,3:]

        positions = defaultdict(list)
        for idx in range(particles.shape[0]):
            positions[tuple(particles[idx,:3])].append(idx)

        collisions = []
        for indices in positions.values():
            if len(indices) > 1:
                collisions.extend(indices)

        particles = np.delete(particles, collisions, axis=0)
        
    return particles.shape[0]
