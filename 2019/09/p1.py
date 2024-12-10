from collections import defaultdict


def part1(puzzle_input):

    intcode = [int(n) for n in puzzle_input.split(',')]

    nums = defaultdict(int)

    for i, n in enumerate(intcode):
        nums[i] = n

    i = 0
    relative_i = 0
    while nums[i] != 99:
        n = str(nums[i])

        args = {
            1: nums[nums[i+1]] if len(n) < 3 or n[-3] == '0' else nums[i+1] if n[-3] == '1' else nums[relative_i + nums[i+1]],
            2: None if n[-1] == '4' else nums[nums[i+2]] if len(n) < 4 or n[-4] == '0' else nums[i+2] if n[-4] == '1' else nums[relative_i + nums[i+2]]}
        
        write_to = {
            1: nums[i+1] if len(n) < 3 or n[-3] != '2' else relative_i + nums[i+1],
            3: nums[i+3] if len(n) < 5 or n[-5] != '2' else relative_i + nums[i+3]}

        if n[-1] == '1':
            nums[write_to[3]] = args[1] + args[2]
            i += 4

        elif n[-1] == '2':
            nums[write_to[3]] = args[1] * args[2]
            i += 4

        elif n[-1] == '3': 
            nums[write_to[1]] = 1
            i += 2

        elif n[-1] == '4':
            output_val = args[1]
            i += 2

        elif n[-1] == '5':
            i = args[2] if args[1] else i + 3

        elif n[-1] == '6':
            i = args[2] if not args[1] else i + 3

        elif n[-1] == '7': 
            nums[write_to[3]] = 1 if args[1] < args[2] else 0
            i += 4

        elif n[-1] == '8': 
            nums[write_to[3]] = 1 if args[1] == args[2] else 0
            i += 4

        elif n[-1:] == '9':
            relative_i += args[1]
            i += 2

    return output_val