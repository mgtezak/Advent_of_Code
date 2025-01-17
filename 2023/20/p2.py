from collections import deque
from itertools import count
import math

def part2(puzzle_input):
    graph = {}
    flip_flop = {}
    memory = {}
    for line in puzzle_input.split('\n'):
        source, destinations = line.split(' -> ')
        destinations = destinations.split(', ')
        graph[source.lstrip('%&')] = destinations
        if source.startswith('%'):
            flip_flop[source[1:]] = 0   # each flip flip is off (0) by default
        elif source.startswith('&'):
            memory[source[1:]] = {}

    for conjunction in memory.keys():   # get source modules for conjunctions 
        for source, destinatons in graph.items():
            if conjunction in destinatons:
                memory[conjunction][source] = 0   # initialize memory at low (0)

    final_layer = [m1 for m1 in graph if 'rx' in graph[m1]]
    assert len(final_layer) == 1, "Assumption #1: There is only 1 module pointing to rx"
    assert final_layer[0] in memory, "Assumption #2: The final module before rx is a conjunction"

    semi_final_layer = set(module for module in graph if final_layer[0] in graph[module])
    cycle_lengths = []  # Assumption #3: The modules on semi_final_layer signal high in regular intervals / cycles
    
    for button_push in count(1):
        queue = deque([('broadcaster', in_module, 0) for in_module in graph['broadcaster']])
        while queue:
            out_module, in_module, signal = queue.popleft()

            if in_module in flip_flop and signal == 0:
                flip_flop[in_module] = 1 - flip_flop[in_module]
                out_signal = flip_flop[in_module]

            elif in_module in memory:
                memory[in_module][out_module] = signal
                out_signal = 1 if 0 in memory[in_module].values() else 0
                if in_module in semi_final_layer and out_signal == 1:
                    cycle_lengths.append(button_push)
                    semi_final_layer.remove(in_module)

            else:   # no output
                continue
            
            queue.extend([(in_module, nxt, out_signal) for nxt in graph[in_module]])

        if not semi_final_layer:
            break

    return math.lcm(*cycle_lengths)
