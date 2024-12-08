import hashlib

def part1(puzzle_input):
    pw = ''
    i = 1
    while len(pw) < 8:
        hash = hashlib.md5((puzzle_input + str(i)).encode()).hexdigest()
        if hash.startswith('00000'):
            pw += hash[5]
        i += 1
    return pw