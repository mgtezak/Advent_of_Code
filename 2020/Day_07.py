path = 'Advent_of_Code/2020/puzzle_input/07.txt'

import re

with open(path) as input:
    lines = input.read().split('\n')

bags = {}
for line in lines[:]:
    (_, outer), *content = re.findall(r'(\d*) ?(\w+ \w+) bag', line)
    if content[0][0]:
        bags[outer] = {inner: int(n) for n, inner in content}
    else:
        bags[outer] = []

# Part 1:
def get_n_outer_bags(content={'shiny gold'}):
    while True:
        new = set()
        for inner in content:
            new |= {outer for outer in bags if inner in bags[outer]}

        if new.difference(content):
            content |= new
        else:
            return len(content)

# Part 2:
def get_n_inner_bags():
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

print(f'Part 1: {get_n_outer_bags()}')
print(f'Part 2: {get_n_inner_bags()}')