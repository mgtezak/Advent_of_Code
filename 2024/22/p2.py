from collections import defaultdict


def part2(puzzle_input):
    prune_mask = (1 << 24) - 1

    def generate_next(num):
        num ^= (num << 6) & prune_mask
        num ^= (num >> 5) 
        num ^= (num << 11) & prune_mask
        return num

    total_bananas = defaultdict(int)
    for num in map(int, puzzle_input.split('\n')):
        seen = set()
        diffs = []
        for i in range(2000):
            next_num = generate_next(num)
            diffs.append((next_num % 10) - (num % 10))
            num = next_num
            if i >= 3:
                if (sequence := tuple(diffs)) not in seen:
                    total_bananas[sequence] += num % 10
                    seen.add(sequence)
                diffs.pop(0)

    return max(total_bananas.values())
