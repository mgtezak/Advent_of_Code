import re
from operator import __and__, __xor__, __or__


def part1(puzzle_input):
    initial_values, gates = puzzle_input.split('\n\n')

    values = {}
    for wire, value in re.findall(r'(\w+): (0|1)', initial_values):
        values[wire] = int(value)

    wire_map = {}
    for in1, op, in2, out in re.findall(r'(\w+) (AND|XOR|OR) (\w+) -> (\w+)', gates):
        wire_map[out] = (op, in1, in2)

    operators = {
        'AND': __and__,
        'XOR': __xor__,
        'OR': __or__
    }

    def get_value(wire):
        if wire in values:
            return values[wire]
        op, in1, in2 = wire_map[wire]
        values[wire] = operators[op](get_value(in1), get_value(in2))
        return values[wire]
    
    max_bit = max(int(wire[1:]) for wire in wire_map if wire.startswith('z'))
    z_bits = [str(get_value(f'z{i:02}')) for i in range(max_bit + 1)]
    return int(''.join(reversed(z_bits)), 2)
