def part2(puzzle_input):
    disk = []
    for i, num in enumerate(puzzle_input):
        idx = None if i % 2 else i // 2
        size = int(num)
        if size > 0:
            disk.append([idx, size])

    i = 0
    while i < len(disk):
        i += 1
        idx, size = disk[-i]
        if idx is None:
            continue
        
        for j in range(len(disk) - i):
            if disk[j][0] is None and disk[j][1] >= size:
                if disk[j][1] == size:
                    disk[j][0] = idx
                else:
                    disk[j][1] -= size
                    disk.insert(j, disk[-i].copy())
                disk[-i][0] = None
                break

    total = idx = 0
    for id, size in disk:
        if id is not None:
            total += id * size * (idx + ((size - 1) / 2))
        idx += size

    return int(total)
