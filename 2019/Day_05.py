path = 'Advent_of_Code/2019/puzzle_input/05.txt'

with open(path) as input:
    intcode = list(map(int, input.read().split(',')))

def run_intcode(input_val=1):
    nums = intcode.copy()
    i = 0
    while nums[i] != 99:
        n = str(nums[i])

        if n[-1] == '1':
            val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
            val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
            nums[nums[i+3]] = val1 + val2
            i += 4

        elif n[-1] == '2':
            val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
            val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
            nums[nums[i+3]] = val1 * val2
            i += 4

        elif n[-1] == '3':
            nums[nums[i+1]] = input_val
            i += 2

        elif n[-1] == '4':
            output_val = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
            i += 2

        elif n[-1] == '5': # part 2
            val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
            if val1:
                i = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
            else:
                i += 3

        elif n[-1] == '6': # part 2
            val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
            if not val1:
                i = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
            else:
                i += 3

        elif n[-1] == '7': # part 2
            val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
            val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
            nums[nums[i+3]] = 1 if val1 < val2 else 0
            i += 4

        elif n[-1] == '8': # part 2
            val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
            val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
            nums[nums[i+3]] = 1 if val1 == val2 else 0
            i += 4

    return output_val            


print(f'Part 1: {run_intcode()}')
print(f'Part 2: {run_intcode(5)}')