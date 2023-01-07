with open('Advent_of_Code/2015/puzzle_input/14.txt') as input:
    reindeers = [line.split() for line in input.read().split('.\n')]

def get_distance(r, total_secs):
    name, speed, fly_secs, rest_secs = r[0], int(r[3]), int(r[6]), int(r[-2])
    full_fly_cycles = (total_secs // (fly_secs + rest_secs)) * fly_secs
    partial_fly_cycle = min(fly_secs, total_secs % (fly_secs + rest_secs))
    full_distance = (full_fly_cycles + partial_fly_cycle) * speed
    return (full_distance, name)

def get_winnner_by_distance(total_secs=2503):
    winners = sorted([get_distance(r, total_secs) for r in reindeers])
    winners = [r for r in winners if r[0] == winners[-1][0]] ### select multiple if multiple in first place
    return winners
      
def get_winner_by_points():
    points = {r[0]: 0 for r in reindeers}        
    for accumulated_secs in range(1, 2504):
        winners = get_winnner_by_distance(accumulated_secs)
        for r in winners:
            points[r[1]] += 1
    return max(points.values())

print(f'Part 1: {get_winnner_by_distance()[0][0]}')
print(f'Part 2: {get_winner_by_points()}')