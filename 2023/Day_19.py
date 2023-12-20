import re
import operator
import math

with open('Advent_of_Code/2023/puzzle_input/19.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    workflows, parts = puzzle_input.split('\n\n')
    work_regex = r'(\w+)\{([^}]+)\}'
    cond_regex = r'(\w+)(<|>)(\d+):(\w+)'
    flow = {}
    for name, rules in re.findall(work_regex, workflows):
        conditional = re.findall(cond_regex, rules)
        final = rules.split(',')[-1]
        flow[name] = conditional + [final]

    part_regex = r'x=(\d+),m=(\d+),a=(\d+),s=(\d+)'
    comp = {'>': operator.gt, '<': operator.lt}
    total_accepted = 0
    for part in re.findall(part_regex, parts):
        part = dict(zip('xmas', map(int, part)))
        curr = 'in'
        while curr not in ('A', 'R'):
            for cat, op, amt, res in flow[curr][:-1]:
                if comp[op](part[cat], int(amt)):
                    curr = res
                    break
            else:
                curr = flow[curr][-1]

        if curr == 'A':
            total_accepted += sum(part.values())

    return total_accepted


def part2(puzzle_input):
    workflows, parts = puzzle_input.split('\n\n')
    work_regex = r'(\w+)\{([^}]+)\}'
    cond_regex = r'(\w+)(<|>)(\d+):(\w+)'
    flow = {}
    for name, rules in re.findall(work_regex, workflows):
        conditional = []
        for cat, op, amt, res in re.findall(cond_regex, rules):
            conditional.append(('xmas'.index(cat), op, int(amt), res))
        final = rules.split(',')[-1]
        flow[name] = conditional + [final]

    start = ('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000))
    queue = [start]
    total_accepted = 0
    while queue:
        curr, *intervals = queue.pop()
        if curr in ('A', 'R'):
            if curr == 'A':
                total_accepted += math.prod(hi-lo+1 for lo, hi in intervals)
            continue

        for cat_idx, op, amt, res in flow[curr][:-1]:
            lo, hi = intervals[cat_idx]

            # All passthrough, no transfer
            if (op == '>' and amt >= hi) or (op == '<' and amt <= lo):
                continue

            # All transfer no passthrough
            if (op == '>' and amt < lo) or (op == '<' and amt > hi):
                queue.append((res, *intervals))
                break

            # Some of both
            if op == '>':
                transfer = (amt+1, hi)
                passthrough = (lo, amt)
            else:
                transfer = (lo, amt-1)
                passthrough = (amt, hi)
            intervals[cat_idx] = passthrough
            intervals2 = intervals.copy()
            intervals2[cat_idx] = transfer
            queue.append((res, *intervals2))
        
        else: # Remaining is transferred
            queue.append((flow[curr][-1], *intervals))

    return total_accepted


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))