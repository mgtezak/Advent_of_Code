def part1(puzzle_input):
    intcode = list(map(int, puzzle_input.split(',')))
    nums = intcode.copy()
    i = 0
    while nums[i] != 99:
        n = str(nums[i])
        args = {
            1: nums[nums[i+1]] if len(n) < 3 or n[-3] == '0' else nums[i+1],
            2: nums[nums[i+2]] if n[-1] != '4' and (len(n) < 4 or n[-4] == '0') else nums[i+2]}

        if n[-1] == '1':
            nums[nums[i+3]] = args[1] + args[2]
            i += 4

        elif n[-1] == '2':
            nums[nums[i+3]] = args[1] * args[2]
            i += 4

        elif n[-1] == '3':
            nums[nums[i+1]] = 1
            i += 2

        elif n[-1] == '4':
            output_val = args[1]
            i += 2

    return output_val