def part1(puzzle_input):
    prune_mask = (1 << 24) - 1

    def generate_next(num):
        num ^= (num << 6) & prune_mask
        num ^= (num >> 5) 
        num ^= (num << 11) & prune_mask
        return num

    secret_num_total = 0
    for num in map(int, puzzle_input.split('\n')):
        for _ in range(2000):
            num = generate_next(num)
        secret_num_total += num

    return secret_num_total
