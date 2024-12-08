import re


def part2(puzzle_input):

    def decompress(compressed):
        length = 0
        while compressed:
            marker = re.search(r'\((\d+)x(\d+)\)', compressed)
            if marker:
                start, stop = marker.span()
                chars, repeat = map(int, marker.groups())
                length += start + decompress(compressed[stop: stop + chars]) * repeat
                compressed = compressed[stop+chars:]

            else:
                length += len(compressed)
                break
            
        return length
                
    return decompress(puzzle_input)
