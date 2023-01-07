import itertools

with open('Advent_of_Code/2015/puzzle_input/13.txt') as input:
    lines = [line.strip('.').split() for line in input.read().split('\n')]

def get_preferences(lines):
    '''returns list of who preferres/dislikes to sit next to who and how much'''
    preferences = []
    for line in lines:
        sub, obj = line[0], line[-1]
        pref =  int(line[3]) * (1 if line[2] == 'gain' else -1)
        preferences.append((sub, obj, pref))
    return preferences

def get_optimal_arrangement(permutations, preferences):
    '''scores all possible seating arrangements and returns the highest score'''
    compare_happiness = []
    for perm in permutations:
        happiness = 0
        for i, guest in enumerate(perm):
            neighbor = perm[i-1]
            happiness += sum([pref[2] for pref in preferences if (guest in pref and neighbor in pref)])
        compare_happiness.append(happiness)
    winner = max(compare_happiness)
    return winner

# Part 1:                      
guests = set(line[0] for line in lines)
permutations = itertools.permutations(guests)
preferences = get_preferences(lines)
part1 = get_optimal_arrangement(permutations, preferences)

# Part 2:
guests.add('I')
permutations = itertools.permutations(guests)
lines.extend([f'I would gain 0 happiness units by sitting next to {guest}'.split() for guest in guests])
lines.extend([f'{guest} would gain 0 happiness units by sitting next to I'.split() for guest in guests])
preferences = get_preferences(lines)
part2 = get_optimal_arrangement(permutations, preferences)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')