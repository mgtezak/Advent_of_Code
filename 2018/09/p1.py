from collections import deque, defaultdict
import re

def part1(puzzle_input):
    regex = r"(\d+) players; last marble is worth (\d+) points"
    n_players, last_marble = [int(n) for n in re.findall(regex, puzzle_input)[0]]
    circle = deque([0])
    scores = defaultdict(int)

    for n in range(1, last_marble + 1):
        if not n % 23:
            circle.rotate(7)
            scores[n % n_players] += n + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(n)

    return max(scores.values())