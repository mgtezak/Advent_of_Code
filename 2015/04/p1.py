import hashlib


def part1(puzzle_input):
    num = 0
    while True:
        result = hashlib.md5((puzzle_input + str(num)).encode())
        if result.hexdigest()[:5] == '00000':
            break
        num += 1
        
    return num
