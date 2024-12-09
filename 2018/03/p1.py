def part1(puzzle_input):
    claims = [line.split() for line in puzzle_input.split('\n')]
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

    return len([ids for ids in claimed.values() if len(ids) > 1])