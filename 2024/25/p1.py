from collections import defaultdict


def part1(puzzle_input):
    locks_and_keys = defaultdict(list)
    for seg in puzzle_input.split('\n\n'):
        locks_and_keys[seg[0]].append([
            col.count('#') for col in zip(*seg.split('\n'))
        ])
    
    fit = 0
    for lock in locks_and_keys['.']:
        for key in locks_and_keys['#']:
            fit += all(i + j < 8 for i, j in zip(lock, key))
            
    return fit
