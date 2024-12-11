import re

def part2(puzzle_input):
    mem = {}
    for line in puzzle_input.split('\n'):
        if line.startswith('mask'):
            mask = line[7:]
        else:
            address, val = re.findall(r'(\d+)', line)
            address, val = bin(int(address))[2:].zfill(36), int(val)
            masked = ['']
            for i, m in zip(address, mask):
                if m == '0':
                    for j in range(len(masked)):
                        masked[j] += i
                elif m == '1':
                    for j in range(len(masked)):
                        masked[j] += '1'
                else:
                    for j in range(len(masked)):
                        masked.append(masked[j] + '0')
                        masked[j] += '1'

            for address in masked:
                mem[address] = val

    return sum(mem.values())