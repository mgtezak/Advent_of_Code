import re


def part1(puzzle_input):
    times, distances = puzzle_input.split('\n')
    times = map(int, re.findall('\d+', times))
    distances = map(int, re.findall('\d+', distances))
    total = 1
    for t, d in zip(times, distances):
        wins = 0
        for speed in range(1, t):
            travelled = (t-speed) * speed
            if travelled > d:
                wins += 1
            elif wins:
                break

        total *= wins
    
    return total
