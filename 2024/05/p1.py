from collections import defaultdict
import re

def part1(puzzle_input):
    rules, updates = puzzle_input.split('\n\n')
    preceding = defaultdict(set)
    for p1, p2 in re.findall(r'(\d+)\|(\d+)', rules):
        preceding[int(p2)].add(int(p1))

    def get_score(pages):
        disallowed = set()
        for page in pages:
            if page in disallowed:
                return 0
            
            disallowed |= preceding[page]

        return pages[len(pages)//2]

    total = 0
    for line in updates.split('\n'):
        pages = list(map(int, line.split(',')))
        total += get_score(pages)

    return total
