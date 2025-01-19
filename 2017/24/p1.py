import re
from collections import defaultdict


def part1(puzzle_input):
    pairs = re.findall(r'(\d+)/(\d+)', puzzle_input)
    pairs = [list(map(int, pair)) for pair in pairs]
    bridges = defaultdict(list)
    for i, (x, y) in enumerate(pairs):
        bridges[x].append((i, y))
        bridges[y].append((i, x))

    def dfs(num1, score1):
        score2 = 0
        for i, num2 in bridges[num1]:
            if i not in used:
                used.add(i)
                score2 = max(score2, dfs(num2, num1 + num2))
                used.remove(i)

        return score1 + score2

    used = set()
    return dfs(0, 0)
