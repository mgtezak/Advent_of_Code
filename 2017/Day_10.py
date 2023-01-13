path = 'Advent_of_Code/2017/puzzle_input/10.txt'

with open(path) as input:
    input = input.read()

def knot(part2=False):

    # processing input
    if part2:
        ascii_codes = [ord(char) for char in input]
        suffix = [17, 31, 73, 47, 23]
        lengths = ascii_codes + suffix
    else:
        lengths = list(map(int, input.split(',')))
 
    # knotting algorithm:
    circle = [n for n in range(256)]
    pos = 0
    skip_size = 0
    for _ in range(64):
        for l in lengths:
            substring = [circle[i % 256] for i in range(pos, pos + l)]
            while substring:
                circle[pos] = substring.pop()
                pos = (pos + 1) % 256
            pos = (pos + skip_size) % 256
            skip_size += 1

        # part 1 ends after one round
        if not part2: 
            return circle[0] * circle[1]
    
    # processing output for part 2
    knot_hash = ''
    for i in range(16):
        block_val = 0 
        for n in circle[(i * 16): i * 16 + 16]:
            block_val ^= n
        knot_hash += hex(block_val)[2:].zfill(2)
    return knot_hash


print(f'Part 1: {knot()}')
print(f'Part 2: {knot(part2=True)}')