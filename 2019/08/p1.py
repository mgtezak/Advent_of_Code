def part1(puzzle_input, is_example_input=False):
    width = 2 if is_example_input else 25
    height = 2 if is_example_input else 6

    pixels = puzzle_input
    n = width * height
    layers = []
    while pixels:
        layers.append(pixels[:n])
        pixels = pixels[n:]
    
    least_zeros = min((layer.count('0'), layer) for layer in layers)[1]
    return least_zeros.count('1') * least_zeros.count('2')
