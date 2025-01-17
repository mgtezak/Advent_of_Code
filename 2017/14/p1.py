def part1(puzzle_input):

    def hex_to_binary(digit):
        return bin(int(digit, 16))[2:].zfill(4)

    def binary_knot_hash(s):
        ascii_codes = [ord(char) for char in s]
        suffix = [17, 31, 73, 47, 23]
        lengths = ascii_codes + suffix
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

        knot_hash = ''
        for i in range(16):
            block_val = 0 
            for n in circle[(i * 16): i * 16 + 16]:
                block_val ^= n

            knot_hash += hex(block_val)[2:].zfill(2)

        return ''.join(hex_to_binary(digit) for digit in knot_hash)
    
    keys = [f'{puzzle_input}-{i}' for i in range(128)]
    return sum(binary_knot_hash(key).count('1') for key in keys)
