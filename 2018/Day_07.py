path = 'Advent_of_Code/2018/puzzle_input/07.txt'

from copy import deepcopy
from string import ascii_uppercase

# read data:

with open(path) as input:
    instructions = [line.split() for line in input.read().split('\n')]

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
deep_copy = deepcopy(requirements)


# part 1

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


# part2:

requirements = deep_copy
possible_steps = [s for s in all_steps if s not in requirements]
time_required = {s: 61 + ascii_uppercase.index(s) for s in all_steps}
time_elapsed = 0
idle = 5
in_progress = {}

while True:
    possible_steps = sorted(possible_steps, reverse=True)
    for w in range(idle):
        if possible_steps:
            next_step = possible_steps.pop()
            in_progress[next_step] = time_required[next_step]
            idle -= 1

    in_progress = {step: time for step, time in in_progress.items() if time}
    if not in_progress:
        break

    time_elapsed += 1
    for cur_step in in_progress:
        in_progress[cur_step] -= 1
        if not in_progress[cur_step]:
            idle += 1
            for step in requirements:
                if cur_step in requirements[step]:
                    requirements[step].remove(cur_step)
                    if not requirements[step]:
                        possible_steps.append(step)


print(f'Part 1: {order_of_steps}')
print(f'Part 2: {time_elapsed}')