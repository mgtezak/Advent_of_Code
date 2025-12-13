# TODO: try out this much cooler approach: 
# https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/

import z3
from collections import defaultdict

def part2(puzzle_input):
    total_presses = 0
    for line in puzzle_input.splitlines():
        _, *buttons, joltages = line.split()
        joltages = list(map(int, joltages[1:-1].split(',')))
        solver = z3.Optimize()
        button_presses = z3.IntVector("button_presses", len(buttons))

        button_indices = defaultdict(list)
        for i, btn in enumerate(buttons):
            solver.add(button_presses[i] >= 0)
            for j in btn[1:-1].split(','):
                button_indices[int(j)].append(i)

        for j, indices in button_indices.items():
            solver.add(joltages[j] == sum(button_presses[i] for i in indices))

        presses = z3.Sum(button_presses)
        solver.minimize(presses)
        solver.check()
        total_presses += solver.model().eval(presses).as_long()
    
    return total_presses
