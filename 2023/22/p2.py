import re


def part2(puzzle_input):
    regex = r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)'
    blocks = []
    for block in re.findall(regex, puzzle_input):
        x1, y1, z1, x2, y2, z2 = map(int, block)
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        z1, z2 = sorted((z1, z2))
        blocks.append((x1, y1, z1, x2, y2, z2))

    blocks.sort(key=lambda x: x[2]) # sort by z1: distance to ground
    X = max(b[3] for b in blocks) + 1
    Y = max(b[4] for b in blocks) + 1
    Z = max(b[5] for b in blocks) + 1
    N = len(blocks)

    stack = [[['empty' for _ in range(X)] for _ in range(Y)] for _ in range(Z)]
    supported_by = {}
    for block_id, (x1, y1, z1, x2, y2, z2) in enumerate(blocks): 
        # Let block fall until it receives support
        for z in range(Z):
            support = set(stack[z][y][x] for x in range(x1, x2+1) for y in range(y1, y2+1)) - {'empty'}
            if support:
                supported_by[block_id] = support
                break
        # Add block above its support
        height = z2 - z1 + 1
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z_ in range(z-height, z):
                    stack[z_][y][x] = block_id

    # Disintegrate indispensible blocks & examine the resulting chain reactions
    indispensible = set.union(*[x for x in supported_by.values() if len(x)==1])
    total = 0
    for i in indispensible:
        disintegrated = set([i])
        for j in range(i+1, N):
            if j in supported_by and supported_by[j].issubset(disintegrated):
                disintegrated.add(j)
        total += len(disintegrated) - 1

    return total
