def part1(puzzle_input):
    instructions = [line.split() for line in puzzle_input.split('\n')]
    requirements = {}
    all_steps = set()

    for i in instructions:
        earlier, later = i[1], i[7]
        all_steps |= {earlier, later}
        if requirements.get(later):
            requirements[later].append(earlier)
        else:
            requirements[later] = [earlier]

    possible_steps = [s for s in all_steps if s not in requirements]
    order_of_steps = ''
    while possible_steps:
        possible_steps = sorted(possible_steps, reverse=True)
        cur_step = possible_steps.pop()
        order_of_steps += cur_step
        for step in requirements:
            if cur_step in requirements[step]:
                requirements[step].remove(cur_step)
                if not requirements[step]:
                    possible_steps.append(step)

    return order_of_steps