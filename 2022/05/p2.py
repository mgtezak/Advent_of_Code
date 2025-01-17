import re


def part2(puzzle_input):
    sketch, instructions = puzzle_input.split('\n\n')

    sketch = sketch.split('\n')
    m, n = len(sketch), len(sketch[0])
    pos = [[] for _ in range(n//4+1)]
    for j in range(m-1, -1, -1):
        for i in range(1, n, 4):
            if sketch[j][i].isupper():
                pos[i//4].append(sketch[j][i])

    for nums in re.findall(r'(\d+) from (\d+) to (\d+)', instructions):
        q, f, t = map(int, nums)                # q: quantity, f: from, t: to
        crates = pos[f-1][-q:]                  # identify q crates at f
        pos[f-1] = pos[f-1][:-q]                # remove them at f
        pos[t-1] += crates                      # add them at t

    return ''.join(crate[-1] for crate in pos)  # return upper crate of each position
