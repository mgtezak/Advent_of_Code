from itertools import permutations


def part1(puzzle_input):

    lines = [line.strip('.').split() for line in puzzle_input.split('\n')]

    preferences = []
    for line in lines:
        sub, obj = line[0], line[-1]
        pref =  int(line[3]) * (1 if line[2] == 'gain' else -1)
        preferences.append((sub, obj, pref))

    guests = set(line[0] for line in lines)
    compare_happiness = []
    for perm in permutations(guests):
        happiness = 0
        for i, guest in enumerate(perm):
            neighbor = perm[i-1]
            happiness += sum([pref[2] for pref in preferences if (guest in pref and neighbor in pref)])
        compare_happiness.append(happiness)

    return max(compare_happiness)
