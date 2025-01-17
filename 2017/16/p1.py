from string import ascii_lowercase
import re


def part1(puzzle_input, is_example_input=False):
    n = 5 if is_example_input else 16
    programs = list(ascii_lowercase[:n])
    for cmd in puzzle_input.split(','):
        if cmd[0] == 's':
            i = int(cmd[1:])
            programs = programs[-i:] + programs[:-i]
        elif cmd[0] == 'x':
            i, j = map(int, re.findall(r'(\d+)', cmd))
            programs[i], programs[j] = programs[j], programs[i]
        else:
            i = programs.index(cmd[1])
            j = programs.index(cmd[3])
            programs[i], programs[j] = programs[j], programs[i]

    return ''.join(programs)
