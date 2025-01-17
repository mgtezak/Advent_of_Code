from string import ascii_lowercase
import re


def part2(puzzle_input, is_example_input=False):
    n = 5 if is_example_input else 16
    original_order = ascii_lowercase[:n]
    programs = list(original_order)
    total_reps = 1_000_000_000
    history = {0: original_order}
    for rep in range(total_reps):
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

        if (state := ''.join(programs)) in set(history.values()):
            return history[((total_reps % rep) - 1) % rep]
        
        history[rep] = state

    return ''.join(programs)
