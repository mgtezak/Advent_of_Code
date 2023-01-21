# from my puzzle input:
n_players = 405
last_marble = 70953

from collections import deque, defaultdict


def get_highscore(last_marble=last_marble, n_players=n_players):
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


print(f'Part 1: {get_highscore()}')
print(f'Part 2: {get_highscore(100 * last_marble)}')