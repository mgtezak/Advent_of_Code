from string import ascii_uppercase

def part2(puzzle_input, is_example_input=False):
    min_time = 1 if is_example_input else 61
    time_elapsed = 1 if is_example_input else 0

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
    time_required = {s: min_time + ascii_uppercase.index(s) for s in all_steps}
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

    return time_elapsed
