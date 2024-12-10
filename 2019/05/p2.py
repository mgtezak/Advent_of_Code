def part2(puzzle_input):
    nums = list(map(int, puzzle_input.split(',')))
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
            nums[nums[i+1]] = 5
            i += 2

        elif n[-1] == '4':
            output_val = args[1]
            i += 2

        elif n[-1] == '5': # part 2
            i = args[2] if args[1] else i + 3

        elif n[-1] == '6': # part 2
            i = args[2] if not args[1] else i + 3

        elif n[-1] == '7': # part 2
            nums[nums[i+3]] = 1 if args[1] < args[2] else 0
            i += 4

        elif n[-1] == '8': # part 2
            nums[nums[i+3]] = 1 if args[1] == args[2] else 0
            i += 4

    return output_val