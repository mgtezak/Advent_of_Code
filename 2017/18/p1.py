import re
from collections import defaultdict
from string import ascii_lowercase


def part1(puzzle_input):

    def get_value(x):
        if x in ascii_lowercase:
            return registers[x]
        return int(x)

    regex = r'(\w+) (\w)(?: (-?\w+))?'
    instructions = re.findall(regex, puzzle_input)
    registers = defaultdict(int)
    send_frequency = None
    i = 0

    while True:
        ins, x, y = instructions[i]
        match ins:
            case 'set':
                registers[x] = get_value(y)
            case 'add':
                registers[x] += get_value(y)
            case 'mul':
                registers[x] *= get_value(y)
            case 'mod':
                registers[x] %= get_value(y)
            case 'snd':
                send_frequency = get_value(x)
            case 'jgz':
                if get_value(x) > 0:
                    i += get_value(y)
                    continue
            case 'rcv':
                if registers[x]:
                    break

        i += 1

    return send_frequency
