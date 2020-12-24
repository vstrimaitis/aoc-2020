from puzzle import PuzzleContext
from collections import defaultdict

DIRS = {
    "e":  (1, -1, 0),
    "w":  (-1, 1, 0),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
    "ne": (1, 0, -1),
    "nw": (0, 1, -1),
}

def parse(line):
    moves = []
    i = 0
    while i < len(line):
        if line[i] in "ew":
            moves.append(DIRS[line[i]])
            i += 1
        else:
            moves.append(DIRS[line[i:i+2]])
            i += 2
    return moves

def simulate(moves):
    x, y, z = 0, 0, 0
    for dx, dy, dz in moves:
        x, y, z = x+dx, y+dy, z+dz
    return x, y, z

def calc_next(tile, colors):
    x, y, z = tile
    black_neighs = sum([1 for dx, dy, dz in DIRS.values() if colors[(x+dx, y+dy, z+dz)] == 1])
    if colors[tile] == 0:
        if black_neighs == 2:
            return 1
        return 0
    if black_neighs == 0 or black_neighs > 2:
        return 0
    return 1

def expand(colors):
    tiles = list(colors.keys())
    for x, y, z in tiles:
        for dx, dy, dz in DIRS.values():
            t = x+dx, y+dy, z+dz
            if t not in colors:
                colors[t] = 0

with PuzzleContext(year=2020, day=24) as ctx:

    lines = ctx.nonempty_lines
    colors = defaultdict(int)
    for line in lines:
        moves = parse(line)
        x, y, z = simulate(moves)
        colors[(x, y, z)] = colors[(x, y, z)] ^ 1
    ctx.submit(1, len([x for x in colors.values() if x == 1]))

    for i in range(100):
        expand(colors)
        tiles = list(colors.keys())
        new_colors = [calc_next(tile, colors) for tile in tiles]
        for t, c in zip(tiles, new_colors):
            colors[t] = c
        # print(i+1, len([x for x in colors.values() if x == 1]))
    
    ctx.submit(2, len([x for x in colors.values() if x == 1]))
