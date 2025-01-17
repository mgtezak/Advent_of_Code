from operator import add, sub, mul, truediv


def part2(puzzle_input):

    def get_nums(monkeys):
        for monkey in monkeys:
            if type(monkey) == int or monkey.isnumeric():
                monkey =  int(monkey)
            elif monkey in solved:
                monkey = solved[monkey]
            yield monkey

    make_operation         = {'+': add, '-': sub, '*': mul, '/': truediv}
    make_reverse_operation = {'+': sub, '-': add, '*': truediv, '/': mul}
    lines = [line.split(': ') for line in puzzle_input.split('\n')]
    monkeys = {monkey: output for monkey, output in lines}
    solved = {monkey: int(num) for monkey, num in monkeys.items() if num.isnumeric() and monkey != 'humn'}
    unsolved = {monkey: operation.split() for monkey, operation in monkeys.items() if not operation.isnumeric()}

    while unsolved:

        for m1, (m2, op, m3) in unsolved.items():
            m1, m2, m3 = get_nums((m1, m2, m3))

            if type(m1) == int and type(m2) == int:
                if op in ('+', '*'):
                    solved[m3] = int(make_reverse_operation[op](m1, m2))
                else:
                    solved[m3] = int(make_operation[op](m2, m1))
            
            elif type(m1) == int and type(m3) == int:
                solved[m2] = int(make_reverse_operation[op](m1, m3))

            elif type(m2) == int and type(m3) == int:
                solved[m1] = int(make_operation[op](m2, m3))

            elif m1 == 'root':
                for i, m in enumerate((m2, m3)):
                    if type(m) == int:
                        solved[(m2, m3)[1-i]] = m
                        solved['root'] = 0
                
        newly_solwed = [m1 for m1, (m2, _, m3) in unsolved.items() if all(m in solved for m in (m1, m2, m3))]
        for monkey in newly_solwed:
            del unsolved[monkey]
        
    return solved['humn']
