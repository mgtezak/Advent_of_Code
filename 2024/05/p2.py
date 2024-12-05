from collections import defaultdict
import re

def part2(puzzle_input):
    rules, updates = puzzle_input.split('\n\n')
    preceding = defaultdict(set)
    for p1, p2 in re.findall(r'(\d+)\|(\d+)', rules):
        preceding[int(p2)].add(int(p1))

    def get_score(pages, is_reordered=False):
        disallowed_after = dict()
        for i, page in enumerate(pages):
            if page in disallowed_after:
                j = disallowed_after[page]
                reordered = pages[:j] + [page] + pages[j:i] + pages[i+1:]
                return get_score(reordered, True)
            
            for p in preceding[page]:
                if p not in disallowed_after:
                    disallowed_after[p] = i
            
        return pages[len(pages)//2] if is_reordered else 0

    total = 0
    for line in updates.split('\n'):
        pages = list(map(int, line.split(',')))
        total += get_score(pages)

    return total
