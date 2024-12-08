import re
import hashlib

def part1(puzzle_input):
    keys = []
    triplets = {char: [] for char in '0123456789abcdef'}
    i = 0
    while True:
        hash = hashlib.md5(f'{puzzle_input}{i}'.encode()).hexdigest()

        # Check for quintuples
        for char in re.findall(r'([a-f0-9])\1\1\1\1', hash):
            while triplets[char] and triplets[char][0] < i - 1000:
                triplets[char].pop(0)
            keys.extend(triplets[char])
            triplets[char] = []
            keys.sort()

        # Check for triplets 
        if match := re.search(r'([a-f0-9])\1\1', hash):
            triplets[match.group(0)[0]].append(i)

        if len(keys) >= 64 and i > keys[63] + 1000:
            break

        i += 1

    return keys[63]