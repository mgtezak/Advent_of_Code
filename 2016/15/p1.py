import re

def part1(puzzle_input):
    t_curr = 0
    step = 1
    regex = r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)."
    for line in re.findall(regex, puzzle_input):
        t_delta, lim, pos = map(int, line)
        while (pos + t_delta + t_curr) % lim != 0:
            t_curr += step
        step *= lim

    return t_curr