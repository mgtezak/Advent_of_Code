path = 'Advent_of_Code/2017/puzzle_input/07.txt'

def parse(input):
    nodes = dict()
    for line in input.split('\n'):
        line = [s.strip(',()') for s in line.split()]
        node, weight = line[0], int(line[1])
        branches = [] if len(line) == 2 else line[3:]
        nodes[node] = (weight, branches)
    return nodes

with open(path) as input:
    nodes = parse(input.read())

# Part 1:
node = (set(nodes) - set(n for k in nodes for n in nodes[k][1])).pop()
bottom_node = node

# Part 2:
def calc_weight(node): # node's own weight plus weight of branches
    return nodes[node][0] + sum(calc_weight(n) for n in nodes[node][1])

def is_balanced(node): # True if each branch has the same weight
    return True if len(set(calc_weight(n) for n in nodes[node][1])) == 1 else False

def calc_avg_weight(node): # average weight of a branch
    return sum(calc_weight(n) for n in nodes[node][1]) / len(nodes[node][1])

while not is_balanced(node):
    sorted_branches = sorted(nodes[node][1], key=lambda x: -abs(calc_weight(x) - calc_avg_weight(node))) # puts the outlier in front of the list
    outlier = sorted_branches[0]
    node = outlier

deviation = calc_weight(outlier) - calc_weight(sorted_branches[1])
target_weight = nodes[outlier][0] - deviation

print(f'Part 1: {bottom_node}')
print(f'Part 2: {target_weight}')