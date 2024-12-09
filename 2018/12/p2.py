import re

def part2(puzzle_input):
    state, transitions = puzzle_input.split('\n\n')
    state = set(i for i, pot in enumerate(state.split()[2]) if pot == '#')
    transitions = set(re.findall(r'(.*) => #', transitions))

    def get_next(state):
        nxt = set()
        hi, lo = max(state), min(state)
        for i in range(lo - 2, hi + 3):
            seq = ''.join('#' if j in state else '.' for j in range(i - 2, i + 3))
            if seq in transitions:
                nxt.add(i)
        return nxt

    for gen in range(500):
        if gen == 499:
            prev = sum(state)
        state = get_next(state)

    diff = sum(state) - prev
    return prev + (50_000_000_000 - gen) * diff