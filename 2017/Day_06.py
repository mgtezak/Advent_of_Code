path = 'Advent_of_Code/2017/puzzle_input/06.txt'

with open(path) as input:
    blocks = [int(x) for x in input.read().split()]
    
visited = dict()
cycles = 0
loop_detected = False

while not loop_detected:
    visited[tuple(blocks)] = cycles
    cycles += 1

    qty = max(blocks)
    pos = blocks.index(qty)
    blocks[pos] -= qty
    for i in range(qty):
        blocks[(pos + 1 + i) % 16] += 1

    if tuple(blocks) in visited:
        loop_detected = cycles

loop_size = loop_detected - visited[tuple(blocks)]

print(f'Part 1: {loop_detected}')
print(f'Part 2: {loop_size}')