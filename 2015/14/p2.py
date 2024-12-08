def part2(puzzle_input, is_example_input=False):
    stop_time = 1000 if is_example_input else 2503
    
    def get_distance(r, total_secs):
        name, speed, fly_secs, rest_secs = r[0], int(r[3]), int(r[6]), int(r[-2])
        full_fly_cycles = (total_secs // (fly_secs + rest_secs)) * fly_secs
        partial_fly_cycle = min(fly_secs, total_secs % (fly_secs + rest_secs))
        full_distance = (full_fly_cycles + partial_fly_cycle) * speed
        return (full_distance, name)

    def get_winnner_by_distance(total_secs):
        winners = sorted([get_distance(r, total_secs) for r in reindeers])
        winners = [r for r in winners if r[0] == winners[-1][0]] ### select multiple if multiple in first place
        return winners

    reindeers = [line.split() for line in puzzle_input.split('.\n')]
    points = {r[0]: 0 for r in reindeers}        
    for accumulated_secs in range(1, stop_time + 1):
        winners = get_winnner_by_distance(accumulated_secs)
        for r in winners:
            points[r[1]] += 1

    return max(points.values())
