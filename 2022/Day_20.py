path = 'Advent_of_Code/2022/puzzle_input/20.txt'

with open(path) as input:
    indexed_nums = [(i, n) for i, n in enumerate(map(int, input.read().split('\n')))]

def get_coord_sum(indexed_nums=indexed_nums, n_rounds=1):
    
    mixed = indexed_nums.copy()
    l = len(mixed) - 1

    for _ in range(n_rounds):   # only once in part 1
        for i, n in indexed_nums:
            idx = mixed.index((i, n))
            new_idx = (idx + n) % l
            mixed.remove((i, n))
            mixed.insert(new_idx, (i, n))

    zero_idx = [i for i, tup in enumerate(mixed) if not tup[1]].pop()
    return sum(mixed[(zero_idx + i) % (l+1)][1] for i in (1000, 2000, 3000))

# part 2:
dec_key = 811589153
dec_indexed_nums = [(i, dec_key * n) for i, n in indexed_nums]

print(f'Part 1: {get_coord_sum()}')
print(f'Part 2: {get_coord_sum(dec_indexed_nums, 10)}')