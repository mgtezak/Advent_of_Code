import re

def part2(puzzle_input):

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

    def dfs(unvisited: list, current_v: str='AA', total: int=0, time: int=0, max_time: int=26, elephant: bool=True) -> None:
        
        if elephant and len(unvisited) == 8:
            dfs(unvisited=unvisited, current_v='AA', total=total, max_time=26, elephant=False)
            
        for next_v in unvisited:
            if (distances[current_v][next_v] > max_time - time):
                continue

            unvisited_ = [u for u in unvisited if u != next_v]
            time_      = time + distances[current_v][next_v]
            total_     = total + calc_release(current_v, next_v, time, max_time, distances, release_rates)
            dfs(unvisited_, next_v, total_,time_, max_time)
        
        total_release.add(total)

    regex = r'Valve ([\w]+) has flow rate=([\d]+); tunnels? leads? to valves? (([\w]+,\s)*[\w]+)'
    connections = {}
    release_rates = {}
    for line in puzzle_input.split('\n'):
        valve, rate, connected, _ = re.findall(regex, line)[0]
        connections[valve] = connected.split(', ')
        if rate != '0': 
            release_rates[valve] = int(rate)
            
    distances = dict()
    for v in ['AA'] + list(release_rates):
        distances[v] = {r: 1 + calc_distance(v, r, connections) for r in release_rates if r != v}
    total_release = set()
    dfs(release_rates.keys())
    return max(total_release)
