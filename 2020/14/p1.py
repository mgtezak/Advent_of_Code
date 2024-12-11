import re

def part1(puzzle_input):
    mem = {}
    for line in puzzle_input.split('\n'):
        if line.startswith('mask'):
            mask = line[7:]
        else:
            address, val = re.findall(r'(\d+)', line)
            val = bin(int(val))[2:].zfill(36)
            masked = ''
            for i, m in zip(val, mask):
                masked += i if m == 'X' else m
            mem[address] = int(masked, 2)

    return sum(mem.values())