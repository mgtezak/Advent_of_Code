import re


def part2(puzzle_input):
    layers = [(int(l), int(r)) for l, r in re.findall(r'(\d+): (\d+)', puzzle_input)]
    
    delay = 0
    while True:
        for l, r in layers:
            if (l + delay) % ((r - 1) * 2) == 0:
                delay += 1
                break
        else:
            break

    return delay
