path = 'Advent_of_Code/2019/puzzle_input/02.txt'

with open(path) as input:
    data = input.read().split(',')

def calc(noun, verb, part2=False):
    l = list(map(int, data))
    l[1], l[2] = noun, verb
    for i, val in enumerate(l):
        if i % 4 == 0:  
            if val == 1:
                l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
            elif val == 2:
                l[l[i+3]] = l[l[i+1]] * l[l[i+2]]
            elif val == 99:
                break
    return l[0] == 19690720 if part2 else l[0] 
        
def get_noun_verb_comb():
    for noun in range(100):
        for verb in range(100):
            if calc(noun, verb, True):
                return 100 * noun + verb

print(f'Part 1: {calc(12, 2)}')
print(f'Part 2: {get_noun_verb_comb()}')
