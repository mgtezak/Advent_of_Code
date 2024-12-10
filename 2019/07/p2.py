from itertools import permutations

def part2(puzzle_input):
    intcode = list(map(int, puzzle_input.split(',')))

    def run_intcode(input_vals, nums=intcode.copy(), i=0):
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
                if input_vals:
                    nums[nums[i+1]] = input_vals.pop(0)
                    i += 2
                else:
                    return output_val, nums, i

            elif n[-1] == '4':
                output_val = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                i += 2

            elif n[-1] == '5':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                if val1:
                    i = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                else:
                    i += 3

            elif n[-1] == '6':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                if not val1:
                    i = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                else:
                    i += 3

            elif n[-1] == '7':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                nums[nums[i+3]] = 1 if val1 < val2 else 0
                i += 4

            elif n[-1] == '8':
                val1 = nums[i+1] if len(n) >= 3 and n[-3] == '1' else nums[nums[i+1]]
                val2 = nums[i+2] if len(n) == 4 else nums[nums[i+2]]
                nums[nums[i+3]] = 1 if val1 == val2 else 0
                i += 4

        return output_val, nums, 'done'            

    def get_thruster_signal(perm):
        output = 0
        i = 0
        amp = 0
        states = {x: [None, None] for x in range(5)}

        while states[4][1] != 'done':
            if perm:
                n = perm.pop(0)
                input = [n, output]
                nums = intcode.copy()
                i = 0
            else:
                input = [output]
                nums, i = states[amp]

            output, nums, i = run_intcode(input, nums, i)
            
            states[amp] = [nums, i]
            amp = (amp + 1) % 5

        return output

    perms2 = list(permutations([5, 6, 7, 8, 9]))
    return max(get_thruster_signal(list(p)) for p in perms2)