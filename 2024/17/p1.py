import re


def part1(puzzle_input):
    register, program = puzzle_input.split('\n\n')
    register = dict(zip('ABC', map(int, re.findall(r'\d+', register))))
    program = [int(i) for i in re.findall(r'\d+', program)]
    n = len(program)

    def combo(operand):
        if operand == 4:
            return register['A']
        if operand == 5:
            return register['B']
        if operand == 6:
            return register['C']
        return operand
    
    i = 0
    out = []
    while i < n:
        opcode, operand = program[i:i+2]
        match opcode:
            case 0:
                register['A'] >>= combo(operand)
            case 1:
                register['B'] ^= operand
            case 2:
                register['B'] = combo(operand) % 8
            case 3:
                if register['A']:
                    i = operand - 2
            case 4:
                register['B'] ^= register['C']
            case 5:
                out.append(combo(operand) % 8)
            case 6:
                register['B'] = register['A'] >> combo(operand)
            case 7:
                register['C'] = register['A'] >> combo(operand)
        i += 2

    return ','.join(str(i) for i in out)
