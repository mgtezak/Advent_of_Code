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
    mul_count = 0
    i = 0
    n = len(instructions)
    while 0 <= i < n:
        ins, x, y = instructions[i]
        match ins:
            case 'set':
                registers[x] = get_value(y)
            case 'sub':
                registers[x] -= get_value(y)
            case 'mul':
                registers[x] *= get_value(y)
                mul_count += 1
            case 'jnz':
                if get_value(x) != 0:
                    i += get_value(y)
                    continue
        i += 1

    return mul_count
