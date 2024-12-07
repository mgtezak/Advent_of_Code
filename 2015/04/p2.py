import hashlib


def part2(puzzle_input):
    num = 0
    while True:
        result = hashlib.md5((puzzle_input + str(num)).encode())
        if result.hexdigest()[:6] == '000000':
            break
        num += 1
        
    return num
