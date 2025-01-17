def part1(puzzle_input):

    monkeys = [[line.split() for line in monkey.split('\n')] for monkey in puzzle_input.split('\n\n')]
    m_items = dict()                                   # will track which monkey has which item
    m_inspect = {m: 0 for m, _  in enumerate(monkeys)} # will count how often each monkey will inspect an item
    m_attrs = dict()                                   # tuple of operation and test each monkey performs
    lcm = 1                                            # least common multiple of each monkeys divisor (in this case simply product, since they're all primes)

    for m in monkeys:
        num = int(m[0][1].strip(':'))

        items = [int(i.strip(',')) for i in m[1][2:]]
        m_items[num] = items

        op = tuple(m[2][-2:])                                   # (operator, operand) e. g.: ('*', 17))
        test = tuple(map(int, [m[3][-1], m[4][-1], m[5][-1]]))  # (divisible by, if true, if false)
        lcm *= int(m[3][-1])
        m_attrs[num] = (op, test)

    for _ in range(20):

        for monkey in range(len(monkeys)):

            m_inspect[monkey] += len(m_items[monkey])
            for item in m_items[monkey]:

                op, test = m_attrs[monkey]

                if op[1] == 'old':
                    item **= 2
                elif op[0] == '*':
                    item *= int(op[1])
                else:
                    item += int(op[1])

                item //= 3

                item %= lcm   # x is divisble by y iff x % (multiple of y) is divisble by y
                               
                if item % test[0] == 0:
                    m_items[test[1]].append(item)
                else:
                    m_items[test[2]].append(item)

            m_items[monkey] = []

    a, b = sorted(m_inspect.values())[-2:]
    return a * b
