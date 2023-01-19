path = 'Advent_of_Code/2016/puzzle_input/10.txt'

with open(path) as input:
    lines = [line.split() for line in input.read().split('\n')]

def give_to(type, id, val):
    if type == 'bot':
        if bots.get(id):
            bots[id].append(val)
            fully_loaded.append(id)
        else:
            bots[id] = [val]
    else:
        outputs[id] = val

bots = {}
outputs = {}
fully_loaded = []

for line in lines:
    if line[0] == 'value':
        val, bot_id = line[1], line[-1]
        give_to('bot', bot_id, int(val))

while fully_loaded:
    bot_id = fully_loaded.pop()
    for line in lines:
        if line[0] == 'bot' and line[1] == bot_id:
            low, high = sorted(bots[bot_id])
            if (low, high) == (17, 61):
                part1 = bot_id
            give_to(line[5], line[6], low)
            give_to(line[-2], line[-1], high)

from math import prod
part2 = prod(outputs[f'{i}'] for i in range(3))

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')