from operator import add, sub, mul, truediv


def part1(puzzle_input):
    make_operation = {'+': add, '-': sub, '*': mul, '/': truediv}
    lines = [line.split(': ') for line in puzzle_input.split('\n')]
    monkeys = {monkey: output for monkey, output in lines}

    def get_num(m1):
        output = monkeys[m1]
        if output.isnumeric():
            return int(output)

        m2, op, m3 = output.split()
        m2 = get_num(m2)
        m3 = get_num(m3)
        return int(make_operation[op](m2, m3))

    return get_num('root')
