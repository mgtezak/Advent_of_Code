def part2(puzzle_input):
    blocks = [int(x) for x in puzzle_input.split()]
    n = len(blocks)
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
            blocks[(pos + 1 + i) % n] += 1

        if tuple(blocks) in visited:
            loop_detected = cycles

    return loop_detected - visited[tuple(blocks)]