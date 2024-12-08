from math import prod


def part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]

    def give_to(type, id, val):
        if type == 'bot':
            if bots.get(id):
                bots[id].append(val)
                fully_loaded.append(id)
            else:
                bots[id] = [val]
        else:
            outputs[id] = val

    bots = {}
    outputs = {}
    fully_loaded = []

    for line in lines:
        if line[0] == 'value':
            val, bot_id = line[1], line[-1]
            give_to('bot', bot_id, int(val))

    while fully_loaded:
        bot_id = fully_loaded.pop()
        for line in lines:
            if line[0] == 'bot' and line[1] == bot_id:
                low, high = sorted(bots[bot_id])
                give_to(line[5], line[6], low)
                give_to(line[-2], line[-1], high)

    return prod(outputs[str(i)] for i in range(3))