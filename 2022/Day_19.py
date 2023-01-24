'''
Runtime is around 100 seconds. Not the fastest solution but it works. Not sure how to speed it up further.
I wonder whether there's a vectorized way of calculating {options} and {t_deltas}. At the moment these quite 
elaborate list comprehensions are definitely the weakest link.
'''

path = 'Advent_of_Code/2022/puzzle_input/19.txt'

import re
import numpy as np
import math

regex = re.compile('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')

with open(path) as input:
    blueprints = dict()
    for b in input.read().split('\n'):
        nums = list(map(int, *regex.findall(b)))
        costs = np.array([[nums[1], 0, 0, 0],[nums[2], 0, 0, 0],[nums[3], nums[4], 0, 0], [nums[5], 0, nums[6], 0]])
        max_demand = np.array([max(nums[1], nums[2], nums[3], nums[5]), nums[4], nums[6], math.inf])
        blueprints[nums[0]] = (costs, max_demand)


def get_max_geodes(bp, t_max=24):

    def dfs(robots=np.array([1,0,0,0]), resources=np.array([0,0,0,0]), t=0) -> None:
        '''depth first search algorhythm that searches all interesting strategies'''

        t_left = t_max - t
        options = [i for i in range(4) if (robots[i] < max_demand[i]) and all((robots[j] > 0) or not costs[i,j] for j in range(4))]
        t_deltas = [1 + max(max(0, math.ceil((res - resources[i]) / robots[i])) for i, res in enumerate(costs[j]) if res) for j in options]
        
        for robot, t_delta in zip(options, t_deltas):                          # Skipping bots that take too long and those of whose resources I have plenty
            if (t_delta >= t_left) or (robot != 3 and resources[robot] > 15):  # 15 was the lowest number where I still got the correct result 
                continue                                                       # Hopefully this is true for other peoples puzzle input as well

            new_t = t + t_delta
            new_resources = resources + t_delta * robots - costs[robot]
            new_robots = robots.copy()
            new_robots[robot] += 1
            dfs(new_robots, new_resources, new_t)

        geodes = resources[3] + robots[3] * t_left  # Can't build useful bots anymore but there might still be time left to gather geodes
        results.append(geodes)
    

    costs, max_demand = blueprints[bp]
    results = []
    dfs()
    return max(results)


quality_levels_sum = sum(get_max_geodes(bp) * bp for bp in blueprints)
first_three_prod = math.prod([get_max_geodes(i, t_max=32) for i in range(1, 4)])

print(f'Part 1: {quality_levels_sum}')
print(f'Part 2: {first_three_prod}')