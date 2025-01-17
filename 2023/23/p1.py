from collections import defaultdict


def part1(puzzle_input):
    grid = [list(row) for row in puzzle_input.split('\n')]
    start = (1, 1)       # starting at second tile to prevent the search from going backwards and out of bounds
    target = (len(grid)-1, len(grid[0])-2)

    # create graph where the nodes are the intersections of the grid
    graph = defaultdict(list)
    queue = [(start, start, {start, (0, 1)}, 0)]
    while queue:
        curr_xy, prev_node, visited, slope = queue.pop()
        if curr_xy == target:
            graph[prev_node].append((curr_xy, len(visited)-1))
            continue

        (x, y) = curr_xy
        neighbors = []
        directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        upward_slopes = '^v<>'
        for (i, j), upward in zip(directions, upward_slopes):
            if (i, j) not in visited and (tile := grid[i][j]) != '#':
                tile_slope = 0 if tile == '.' else 1 if tile == upward else -1
                neighbors.append(((i, j), tile_slope))
        
        if len(neighbors) == 1:                                 # neither intersection nor dead end
            nxt_xy, tile_slope = neighbors.pop()
            if tile_slope:
                assert slope + tile_slope != 0, "assumed not to happen: an upward and a downward slope in a single path"
                slope = tile_slope
            queue.append((nxt_xy, prev_node, visited|{nxt_xy}, slope))

        elif len(neighbors) > 1:                                # found an intersection (= node)
            steps = len(visited) - 1
            if (curr_xy, steps) in graph[prev_node] or \
                  (prev_node, steps) in graph[curr_xy]:         # already been here
                continue
            if slope < 1:
                graph[prev_node].append((curr_xy, steps))
            if slope > -1:
                graph[curr_xy].append((prev_node, steps))    
            while neighbors:                                    # traverse paths from current node
                nxt_xy, tile_slope = neighbors.pop()
                queue.append((nxt_xy, curr_xy, {curr_xy, nxt_xy}, tile_slope))

    # traverse graph
    possible_paths = []
    queue = [(start, 0, {start})]
    while queue:
        curr, steps, visited = queue.pop()
        if curr == target:
            possible_paths.append(steps)
            continue
        for nxt, add_steps in graph[curr]:
            if nxt not in visited:
                queue.append((nxt, steps+add_steps, visited|{nxt}))

    return max(possible_paths)
