from collections import deque


def part1(puzzle_input):
    disk = deque([int(size) for size in puzzle_input])
    left_id = 0
    right_id = len(puzzle_input) // 2
    idx = 0
    total = 0
    is_empty_slot = False
    while disk:
        size = disk.popleft()
        if is_empty_slot:
            for _ in range(size):
                total += idx * right_id
                idx += 1
                disk[-1] -= 1
                if disk[-1] == 0:
                    for _ in range(2):
                        disk.pop()
                    right_id -= 1
        else:
            for _ in range(size):
                total += idx * left_id
                idx += 1
            left_id += 1
        is_empty_slot = not is_empty_slot

    return total
