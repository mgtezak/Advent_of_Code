import hashlib

def part2(puzzle_input):
    pw = {}
    i = 1
    while len(pw) < 8:
        hash = hashlib.md5((puzzle_input + str(i)).encode()).hexdigest()
        if (hash.startswith('00000') and \
            hash[5].isnumeric() and \
            int(hash[5]) in range(8) and \
            int(hash[5]) not in pw):                    
                pw[int(hash[5])] = hash[6]
        i += 1
    return ''.join(pw[i] for i in range(8))