import re
from collections import deque, defaultdict
from string import ascii_lowercase


def part2(puzzle_input):

    def get_value(x, id):
        if x in ascii_lowercase:
            return registers[id][x]
        return int(x)

    regex = r'(\w+) (\w)(?: (-?\w+))?'
    instructions = re.findall(regex, puzzle_input)
    indices = [0, 0]
    queues = [deque(), deque()]
    registers = [defaultdict(int), defaultdict(int)]
    registers[1]['p'] = 1
    total_sends = 0
    id = 0

    while True:
        i = indices[id]
        register = registers[id]
        rcv_queue = queues[id]
        snd_queue = queues[1-id]

        while True:
            ins, x, y = instructions[i]
            match ins:
                case 'set':
                    register[x] = get_value(y, id)
                case 'add':
                    register[x] += get_value(y, id)
                case 'mul':
                    register[x] *= get_value(y, id)
                case 'mod':
                    register[x] %= get_value(y, id)
                case 'snd':
                    snd_queue.append(get_value(x, id))
                    total_sends += id == 1
                case 'jgz':
                    if get_value(x, id) > 0:
                        i += get_value(y, id)
                        continue
                case 'rcv':
                    if not rcv_queue:
                        indices[id] = i
                        break
                    register[x] = rcv_queue.popleft()

            i += 1

        id = 1 - id
        if not any(queues):
            break

    return total_sends
