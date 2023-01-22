path = 'Advent_of_Code/2019/puzzle_input/08.txt'

with open(path) as input:
    pixels = input.read()

# Part 1:

n_pixels = 25 * 6
layers = []
while pixels:
    layers.append(pixels[:n_pixels])
    pixels = pixels[n_pixels:]

least_zeros = min((layer.count('0'), layer) for layer in layers)[1]
part1 = least_zeros.count('1') * least_zeros.count('2')


# Part 2:

from collections import defaultdict

image = defaultdict(str)
for layer in layers:
    for i, p in enumerate(layer):
        if p in ('0', '1') and not image[i]:
            image[i] = ' ' if p == '0' else '#'

lines = [[] for _ in range(6)]
for i in range(n_pixels):
    line = i // 25
    lines[line].append(image[i])

rendered_image = '\n' + '\n'.join(''.join(line) for line in lines)

print(f'Part 1: {part1}')
print(f'Part 2: {rendered_image}')