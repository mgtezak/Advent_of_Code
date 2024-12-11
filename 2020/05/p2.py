def part2(puzzle_input):

    boarding_passes = puzzle_input.split('\n')
    occupied = {i: [] for i in range(128)}

    for b in boarding_passes:
        row_partitioning = b[:7]
        col_partitioning = b[7:]

        # find row
        r_low, r_high = 0, 127
        for p in row_partitioning:
            if p == 'F':
                r_high = r_low + (r_high - r_low) // 2
            else:
                r_low = r_low + (r_high - r_low) // 2 + 1
        row = r_low
        
        # find col
        c_low, c_high = 0, 7         
        for p in col_partitioning:
            if p == 'L':
                c_high = c_low + (c_high - c_low) // 2
            else:
                c_low = c_low + (c_high - c_low) // 2 + 1
        col = c_low
        occupied[row].append(col)

    middle_of_plane = False

    for row in occupied:
        if len(occupied[row]) == 8:
            middle_of_plane = True

        elif middle_of_plane and len(occupied[row]) < 8:
            my_seat_id = row * 8 + [i for i in range(8) if i not in occupied[row]].pop()
            break

    return my_seat_id