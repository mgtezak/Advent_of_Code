path = 'Advent_of_Code/2016/puzzle_input/09.txt'

import re

with open(path) as input:
    compressed = input.read()

def decompress(compressed=compressed, part2=False):
    length = 0
    while compressed:
        marker = re.search(r'\((\d+)x(\d+)\)', compressed)
        if marker:
            start, stop = marker.span()
            chars, repeat = map(int, marker.groups())
            if not part2:
                length += start + chars * repeat
            elif part2:
                length += start + decompress(compressed[stop: stop + chars]) * repeat
            compressed = compressed[stop+chars:]

        else:
            length += len(compressed)
            compressed = False
            
    return length


print(f'Part 1: {decompress()}')
print(f'Part 2: {decompress(part2=True)}')