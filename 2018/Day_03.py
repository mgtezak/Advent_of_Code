path = 'Advent_of_Code/2018/puzzle_input/03.txt'

with open(path) as input:
    claims = [line.split() for line in input.read().split('\n')]

claimed = dict()
for c in claims:
    claim_id = int(c[0].strip('#'))
    left, up = [int(n.strip(':')) for n in c[2].split(',')]
    width, height = [int(n) for n in c[3].split('x')]
    for x in range(left, left + width):
        for y in range(up, up + height):
            if claimed.get((x, y)):
                claimed[(x, y)].append(claim_id)
            else:
                claimed[(x, y)] = [claim_id]

claimed_twice = [ids for ids in claimed.values() if len(ids) > 1]
part1 = len(claimed_twice)

all_claim_ids = {n+1 for n in range(len(claims))}
part2 = all_claim_ids.difference({i for ids in claimed_twice for i in ids}).pop()

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')