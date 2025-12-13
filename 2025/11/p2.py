from functools import cache

def part2(puzzle_input):
    connections = {}
    for line in puzzle_input.splitlines():
        input, outputs = line.split(": ")
        connections[input] = outputs.split()
    
    @cache
    def dfs(device, fft, dac):
        if device == "out":
            return 1 if fft and dac else 0
        if (outputs := connections.get(device)) is None:
            return 0
        if device == "fft":
            fft = True
        elif device == "dac":
            dac = True
        return sum(dfs(out, fft, dac) for out in outputs)

    return dfs('svr', False, False)
