import re


def part1(puzzle_input):
    length = 0
    while puzzle_input:
        marker = re.search(r'\((\d+)x(\d+)\)', puzzle_input)
        if marker:
            start, stop = marker.span()
            chars, repeat = map(int, marker.groups())
            length += start + chars * repeat
            puzzle_input = puzzle_input[stop+chars:]

        else:
            length += len(puzzle_input)
            break
        
    return length
