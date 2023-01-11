import re

path = 'Advent_of_Code/2022/puzzle_input/16.txt'

def read_data() -> tuple:
    with open(path) as input:
        valve_layout = input.read().split('\n')
    pattern = re.compile(r'Valve ([\w]+) has flow rate=([\d]+); tunnels? leads? to valves? (([\w]+,\s)*[\w]+)')
    connections = dict()
    release_rates = dict()
    for v in valve_layout:
        valve, rate, connected, _ = re.findall(pattern, v)[0]
        connections[valve] = connected.split(', ')
        if rate != '0': 
            release_rates[valve] = int(rate)
    return connections, release_rates


def calc_distance(start: str, end: str, connections: dict) -> int:
    queue = [(start, 0)]
    visited = [start]
    while len(queue) > 0:
        node, steps = queue.pop(0)
        steps += 1
        for n in connections[node]:
            if n not in visited:
                visited.append(n)
                queue.append((n, steps))
            if n == end:
                return steps


def calc_release(start: str, end: str, t: int, max_t: int, distances: dict, release_rates: dict) -> int:
    payoff_time = max(max_t - t - distances[start][end], 0)
    total_release = payoff_time * release_rates[end]
    return total_release


def get_optimal_path(distances: dict, release_rates: dict, part2: bool=False) -> int:

    def get_valid_paths(unvisited: list=release_rates.keys(), current_v: str='AA', total: int=0, time: int=0, max_time: int=30, elephant: bool=False) -> None:
        
        if elephant and len(unvisited) == 8:
            get_valid_paths(unvisited=unvisited, current_v='AA', total=total, max_time=26, elephant=False)
            
        for next_v in unvisited:
            if (distances[current_v][next_v] > max_time - time):
                continue

            unvisited_ = [u for u in unvisited if u != next_v]
            time_      = time + distances[current_v][next_v]
            total_     = total + calc_release(current_v, next_v, time, max_time, distances, release_rates)

            get_valid_paths(unvisited_, next_v, total_,time_, max_time, elephant)
        
        total_release.add(total)

    total_release = set()

    if part2 == False:
        get_valid_paths()
    else:
        get_valid_paths(max_time=26, elephant=True)

    return max(total_release)


def get_max_release(part2: bool=False) -> int:
    connections, release_rates = read_data()
    distances = dict()
    for v in ['AA'] + list(release_rates):
        distances[v] = {r: 1 + calc_distance(v, r, connections) for r in release_rates if r != v}
    return get_optimal_path(distances, release_rates, part2)


print(f'Part 1: {get_max_release()}')
print(f'Part 1: {get_max_release(part2=True)}')