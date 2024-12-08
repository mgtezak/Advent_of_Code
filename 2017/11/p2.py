def part2(puzzle_input):

    def get_distance(x, y):
        if x * y <= 0:
            return abs(x) + abs(y)
        return min(abs(x), abs(y)) + abs(x-y)
        
    x = y = max_distance = 0
    for step in puzzle_input.split(','):
        if step in ('n', 'nw'):
            x -= 1
        elif step in ('s', 'se'):
            x += 1
        if step in ('sw', 'nw'):
            y -= 1
        elif step in ('ne', 'se'):
            y += 1
        max_distance = max(get_distance(x, y), max_distance)
    
    return max_distance
