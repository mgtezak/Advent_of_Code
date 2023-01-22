path = 'Advent_of_Code/2019/puzzle_input/02.txt'

with open(path) as input:
    instructions = list(map(int, input.read().split(',')))

def run_intcode(noun=12, verb=2):
    nums = instructions.copy()
    nums[1], nums[2] = noun, verb
    for i, val in enumerate(nums):
        if i % 4 == 0:  
            if val == 1:
                nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
            elif val == 2:
                nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
            elif val == 99:
                break
    return nums[0]
        
def get_noun_verb_comb():
    for noun in range(100):
        for verb in range(100):
            if run_intcode(noun, verb) == 19690720:
                return 100 * noun + verb

print(f'Part 1: {run_intcode()}')
print(f'Part 2: {get_noun_verb_comb()}')