from collections import defaultdict
import re

def part2(puzzle_input):
    
    # Parse input
    molecule, reactions = puzzle_input.split('\n\n')

    # Create replacement dictionary
    replace = {}
    for x, y, z in re.findall(r'(\w)(\w) -> (\w)', reactions):
        replace[x + y] = [x + z, z + y]

    # Count (overlapping) pairs
    pairs = defaultdict(int)
    for i in range(len(molecule)-1):
        pairs[molecule[i:i+2]] += 1

    # Execute 40 transition steps
    for _ in range(40):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            for new_pair in replace[pair]:
                new_pairs[new_pair] += count
        pairs = new_pairs

    # Count individual letters in pairs
    letters = defaultdict(int)
    letters[molecule[0]] = 1
    for pair, count in pairs.items():
        letters[pair[1]] += count

    # Return difference between most and least frequent letter
    letter_counts = sorted(letters.values())
    return letter_counts[-1] - letter_counts[0]