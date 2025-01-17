import re
import operator


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
