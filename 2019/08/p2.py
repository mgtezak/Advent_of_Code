from collections import defaultdict


def part2(puzzle_input, is_example_input=False):
    width = 2 if is_example_input else 25
    height = 2 if is_example_input else 6

    pixels = puzzle_input
    n = width * height
    layers = []
    while pixels:
        layers.append(pixels[:n])
        pixels = pixels[n:]
    image = defaultdict(str)
    for layer in layers:
        for i, p in enumerate(layer):
            if p in ('0', '1') and not image[i]:
                image[i] = ' ' if p == '0' else '#'

    lines = [[] for _ in range(height)]
    for i in range(n):
        line = i // width
        lines[line].append(image[i])

    return '\n'.join(''.join(line) for line in lines)
