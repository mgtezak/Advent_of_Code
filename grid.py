from string import ascii_uppercase
import json


SPECIAL_CHARS = "!?.,'"
CHARS = ascii_uppercase + SPECIAL_CHARS


def get_db() -> dict:
    with open('grids.json') as f:
        return json.loads(f.read())


def get_examples():
    return get_db()['examples']


def read(grid):

    def read_chunk(start, end):
        chunk = ''.join(grid[row][start:end] for row in range(m))
        if not chunk.strip():
            return []
        if chunk in charmap:
            return [charmap[chunk]]
        if end-start == 1:
            return [False]
        for mid in range(start+1, end):
            chunk = ''.join(grid[row][start:mid] for row in range(m))
            if chunk in charmap:
                remainder = read_chunk(mid, end)
                if all(remainder):
                    return [charmap[chunk]] + remainder
        return [False]
    
    grid = grid.split('\n')
    charmap = get_db()['grid_to_text']
    chars = []
    m, n = len(grid), len(grid[0])
    delimiters = [col for col in range(n) if all(grid[row][col] == ' ' for row in range(m))] + [n]
    start = 0
    for end in delimiters:
        chunk = read_chunk(start, end)
        chars.extend(chunk if all(chunk) else '_')
        start = end + 1 

    if chars != ['_']:
        return ''.join(chars)
    return '<Unable to decode letter grid>'


def generate(text: str) -> list[str, str, str, str, str]:
    text = text.upper()
    grids_db = get_db()
    small_grid, small_added = _generate(text, grids_db['text_to_grid_small'], 6)
    large_grid, large_added = _generate(text, grids_db['text_to_grid_large'], 10)
    unknown = ''.join(sorted(set(text).difference(set(CHARS)|{' '})))
    return [small_grid, small_added, large_grid, large_added, unknown]


def _generate(text: str, charmap: dict[str, str], height: int) -> tuple[str, str]:
    grid = ['' for _ in range(height)]
    added = set()
    for i, char in enumerate(text):
        if i > 0:
            for j, row in enumerate(charmap['space']):
                grid[j] += row * 2
                
        if char in charmap['added']:
            added.add(char)
        elif char not in charmap:
            if char == ' ':
                char = 'space'
            else:
                char = 'unknown'

        for j, row in enumerate(charmap[char]):
            grid[j] += row
    
    grid = '\n'.join(grid)
    added = ''.join(sorted(added))
    return grid, added
