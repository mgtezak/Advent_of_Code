import math
import re
import numpy as np

def part1(puzzle_input):
    '''Runtime is around 80 seconds. Not the fastest solution but it works. Not sure how to speed it up further.'''

    regex = re.compile('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')
    blueprints = dict()
    for line in puzzle_input.split('\n'):
        bpt, a, b, c, d, e, f = list(map(int, *regex.findall(line)))
        costs = np.array([[a, 0, 0, 0],[b, 0, 0, 0],[c, d, 0, 0], [e, 0, f, 0]])
        max_demand = np.array([max(a, b, c, e), d, f, math.inf])
        blueprints[bpt] = (costs, max_demand)

    def get_max_geodes(bpt, t_max=24):

        def dfs(robots=np.array([1,0,0,0]), resources=np.array([0,0,0,0]), t=0) -> None:
            '''
            Depth-First-Search algorithm, which increments not by minutes but instead 
            by time until the completion of the next robot.
            
            It filters the available production options by:
            (1) Max production demand for given resource. Any production which exceeds the max 
                possible expenditure per minute of that resource is useless.
            (2) Number of resources gathered. If I own more than I can spend (<16 was enough for 
                my puzzle input) then additional production (apart from geodes) is useless.
            (3) Whether the resources for a given bot are even being produced at all.
            (4) Whether time needed to save up for and build robot exceeds time left.

            Once no more useful options are available it fasts-forward to t_max adding up the 
            ongoing geode production.
            '''

            t_left = t_max - t
            options = [i for i in range(4) if (robots[i] < max_demand[i]) and (i == 3 or resources[i] < 16) and all((robots[j] > 0) or not costs[i,j] for j in range(4))]
            t_deltas = [1 + max(max(0, math.ceil((cost - resources[res]) / robots[res])) for res, cost in enumerate(costs[j]) if cost) for j in options]
            
            for robot, t_delta in zip(options, t_deltas):
                if t_delta >= t_left:
                    continue

                new_t = t + t_delta
                new_resources = resources + t_delta * robots - costs[robot]
                new_robots = robots.copy()
                new_robots[robot] += 1
                dfs(new_robots, new_resources, new_t)

            geodes = resources[3] + robots[3] * t_left
            results.append(geodes)
        

        costs, max_demand = blueprints[bpt]
        results = []
        dfs()
        return max(results)

    return sum(get_max_geodes(bpt) * bpt for bpt in blueprints)
