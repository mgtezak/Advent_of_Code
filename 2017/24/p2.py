import re
from collections import defaultdict


def part2(puzzle_input):
    pairs = re.findall(r'(\d+)/(\d+)', puzzle_input)
    pairs = [list(map(int, pair)) for pair in pairs]
    bridges = defaultdict(list)
    for i, (x, y) in enumerate(pairs):
        bridges[x].append((i, y))
        bridges[y].append((i, x))

    def dfs(num1, len1, score1):
        max_len = 0
        max_score = 0
        for i, num2 in bridges[num1]:
            if i not in used:
                used.add(i)
                len2, score2 = dfs(num2, len1 + 1, num1 + num2)
                used.remove(i)
                if len2 == max_len:
                    max_score = max(max_score, score2)
                elif len2 > max_len:
                    max_len = len2
                    max_score = score2

        return len1 + max_len, score1 + max_score

    used = set()
    return dfs(0, 0, 0)[1]
