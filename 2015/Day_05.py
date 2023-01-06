with open('Advent_of_Code/2015/puzzle_input/05.txt') as input:
    strings = input.read().split()

# part 1:
def contains_three_vowels(string):
    count = sum([string.count(v) for v in 'aeiou'])
    if count >= 3:
        return True

def contains_double(string):
    if any(string[i] == string[i+1] for i in range(len(string) - 1)):
        return True

def contains_naughty(string):
    if any(x in string for x in ['ab', 'cd', 'pq', 'xy']):
        return True    

def is_nice_p1(string):
    if contains_three_vowels(string) and contains_double(string) and not contains_naughty(string):
        return True
    return False

# part 2            
def has_repeating_pair(string):
    if any(string[i:i+2] == string[j:j+2] for i in range(len(string)-3) for j in range(i+2, len(string)-1)):
        return True

def repeats_after_gap(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True

def is_nice_p2(string):
    if has_repeating_pair(string) and repeats_after_gap(string):
        return True
    return False        
        
part1 = sum([is_nice_p1(s) for s in strings])
part2 = sum([is_nice_p2(s) for s in strings])

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')