def part1(puzzle_input):

    def backtrack(target, nums):
        n = len(nums)
        queue = [(1, nums[0])]
        while queue:
            i, val = queue.pop()
            if i == n:
                if val == target:
                    return True
                continue
            
            possibilities = [
                val + nums[i],
                val * nums[i],
            ]
            for p in possibilities:
                if p <= target:
                    queue.append((i+1, p))

        return False

    total = 0
    for line in puzzle_input.split('\n'):
        left, right = line.split(': ')
        target = int(left)
        nums = [int(num) for num in right.split()]
        if backtrack(target, nums):
            total += target

    return total
