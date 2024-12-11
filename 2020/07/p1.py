import re

def part1(puzzle_input):

    lines = puzzle_input.split('\n')
    bags = {}

    for line in lines[:]:
        (_, outer), *content = re.findall(r'(\d*) ?(\w+ \w+) bag', line)
        if content[0][0]:
            bags[outer] = {inner: int(n) for n, inner in content}
        else:
            bags[outer] = []

    content = {'shiny gold'}

    while True:
        new = set()
        for inner in content:
            new |= {outer for outer in bags if inner in bags[outer]}

        if new.difference(content):
            content |= new
        else:
            return len(content) - 1   # need to subtract shiny gold bag


def aoc2020_day7_part2(puzzle_input):

    lines = puzzle_input.split('\n')
    bags = {}

    for line in lines[:]:
        (_, outer), *content = re.findall(r'(\d*) ?(\w+ \w+) bag', line)
        if content[0][0]:
            bags[outer] = {inner: int(n) for n, inner in content}
        else:
            bags[outer] = []

    total = 0
    queue = [('shiny gold', 1)]

    while queue:
        outer, n = queue.pop()
        content = bags[outer]
        for inner in content:
            n_inner = n * bags[outer][inner]
            queue.append((inner, n_inner))
            total += n_inner

    return total