# my puzzle input:
door_id = 'cxdnnyjw'

import hashlib

pw_1 = ''
i = 1
while len(pw_1) < 8:
    hash = hashlib.md5((door_id + str(i)).encode()).hexdigest()
    if hash[:5] == '00000':
        pw_1 += hash[5]
    i += 1


pw_2 = {}
i = 1
while len(pw_2) < 8:
    hash = hashlib.md5((door_id + str(i)).encode()).hexdigest()
    if hash[:5] == '00000' and hash[5].isnumeric():
        index = int(hash[5])
        if index in range(8) and index not in pw_2:                    
            pw_2[index] = hash[6]
    i += 1

pw_2 = ''.join(pw_2[i] for i in range(8))


print(f'Part 1: {pw_1}')
print(f'Part 2: {pw_2}')