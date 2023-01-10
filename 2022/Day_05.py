with open('Advent_of_Code/2022/puzzle_input/05.txt') as input:
    lines = [line for line in input.read().split('\n')]

instructions = [list(map(int, line.split()[1:6:2])) for line in lines[10:]]

def read_starting_pos():
    pos = [[] for _ in range(9)]
    start = lines[:9]
    for j in range(8, -1, -1):
        for i in range(1, len(start[j]), 4):
            if start[j][i].isupper():
                pos[int(i/4)].append(start[j][i])   
    return pos

def solve(part2=False):
    pos = read_starting_pos()
    for q, f, t in instructions:                      # q: quantity, f: from, t: to
        crates = pos[f-1][-q:]                        # identify q crates at f
        pos[f-1] = pos[f-1][:-q]                      # remove them at f
        pos[t-1] += crates if part2 else crates[::-1] # add them at t
    return ''.join(crate[-1] for crate in pos)        # return upper crate of each position

print(f'Part 1: {solve()}')
print(f'Part 2: {solve(part2=True)}')