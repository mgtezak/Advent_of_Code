import re
from collections import defaultdict


def part1(puzzle_input):
    segments = puzzle_input.split('\n\n')

    def get_direction(line):
        direction = line.strip('.').split()[-1]
        return 1 if direction == 'right' else -1

    blueprints = {}
    for segment in segments[1:]:
        lines = segment.splitlines()
        state = lines[0][-2]

        write0 = int(lines[2][-2])
        move0 = get_direction(lines[3])
        nxt0 = lines[4][-2]

        write1 = int(lines[6][-2])
        move1 = get_direction(lines[7])
        nxt1 = lines[8][-2]

        blueprints[state] = {
            0: (write0, move0, nxt0),
            1: (write1, move1, nxt1)
        }

    tape = defaultdict(int)
    state = segments[0].split('\n')[0][-2]
    steps = int(re.search(r'(\d+)', segments[0]).group())
    i = 0
    for _ in range(steps):
        write, move, nxt = blueprints[state][tape[i]]
        tape[i] = write
        i += move
        state = nxt

    return sum(tape.values())
