from puzzle import PuzzleContext
from collections import defaultdict

def get_edges(tile):
    n = len(tile)
    m = len(tile[0])
    top, bot, left, right = [], [], [], []
    for i in range(n):
        left.append(tile[i][0])
        right.append(tile[i][-1])
    for j in range(m):
        top.append(tile[0][j])
        bot.append(tile[-1][j])
    return ["".join(top), "".join(bot), "".join(left), "".join(right)]

def rotate_cw(tile):
    t = [list(r) for r in tile]
    return ["".join(list(reversed(x))) for x in zip(*t)]

def flip_v(tile):
    return tile[::-1]

def flip_h(tile):
    new_tile = [r for r in tile]
    n = len(tile)
    m = len(tile[0])
    for i in range(n):
        for j in range(m):
            k = m - j - 1
            if j < k:
                c1 = tile[i][j]
                c2 = tile[i][k]
                new_tile[i] = tile[i][:j] + c1 + tile[i][j+1:k] + c2 + tile[i][k+1:]
    return new_tile

def gen(tile):
    res = []
    tile = flip_h(tile)
    for _ in range(4):
        tile = rotate_cw(tile)
        res.append(tile)
    tile = flip_h(tile)

    tile = flip_v(tile)
    for _ in range(4):
        tile = rotate_cw(tile)
        res.append(tile)
    tile = flip_v(tile)

    return res

def is_above(t1, t2):
    [_,b,_,_] = get_edges(t1)
    [t,_,_,_] = get_edges(t2)
    return t == b

def is_to_the_left(t1, t2):
    [_,_,_,r] = get_edges(t1)
    [_,_,l,_] = get_edges(t2)
    return l == r

def print_grid(grid):
    tile_side = len(grid[0][0])
    n = len(grid) * tile_side
    m = len(grid[0]) * tile_side
    for i in range(n):
        g_i = i // tile_side
        t_i = i % tile_side
        if i % tile_side == 0 and i > 0:
            print()
        for j in range(m):
            g_j = j // tile_side
            t_j = j % tile_side
            if j % tile_side == 0 and j > 0:
                print(" ", end="")
            print(grid[g_i][g_j][t_i][t_j], end="")
        print()
    print()


def try_build_grid(up_left_tile, tiles, corners):
    tiles = tiles.copy()
    corners = corners.copy()
    grid = []

    for i in range(0, side_len):
        grid.append([])
        for j in range(0, side_len):
            if i == 0 and j == 0:
                grid[i].append(up_left_tile)
                del tiles[corners[0]]
                continue
            found = False
            for tile_id, tile in tiles.items():
                is_corner = (i == 0 or i == side_len-1) and (j == 0 or j == side_len-1)
                if not is_corner and tile_id in corners:
                    continue
                if is_corner and tile_id not in corners:
                    continue
                for t in gen(tile):
                    if (j == 0 or is_to_the_left(grid[i][-1], t)) and (i == 0 or is_above(grid[i-1][j], t)):
                        grid[i].append(t)
                        del tiles[tile_id]
                        if tile_id in corners:
                            k = corners.index(tile_id)
                            corners = corners[:k] + corners[k+1:]
                        found = True
                        break
                if found:
                    break
            if not found:
                return None
    return grid

def trim_edges(tile):
    tile = tile[1:-1]
    return [r[1:-1] for r in tile]

def join_grid(grid):
    tile_side = len(grid[0][0])
    n = len(grid) * tile_side
    m = len(grid[0]) * tile_side
    res = []
    for i in range(n):
        row = ""
        g_i = i // tile_side
        t_i = i % tile_side
        for j in range(m):
            g_j = j // tile_side
            t_j = j % tile_side
            row += grid[g_i][g_j][t_i][t_j]
        res.append(row)
    return res

def try_find(grid, pattern):
    n = len(grid)
    m = len(grid[0])
    pn = len(pattern)
    pm = len(pattern[0])
    found = False
    for i in range(n):
        for j in range(m):
            matches = True
            for di in range(pn):
                if not matches:
                    break
                for dj in range(pm):
                    if not matches:
                        break
                    ii = i + di
                    jj = j + dj
                    if ii >= n or jj >= m:
                        matches = False
                        continue
                    if pattern[di][dj] == "#" and grid[ii][jj] != "#":
                        matches = False
            if matches:
                found = True
                for di in range(pn):
                    for dj in range(pm):
                        if pattern[di][dj] == "#":
                            grid[i+di] = grid[i+di][:j+dj] + "X" + grid[i+di][j+dj+1:]
    if not found:
        return None
    return "".join(grid).count("#")

with PuzzleContext(year=2020, day=20) as ctx:
    inputs = ctx.data.split("\n\n")
    tiles = dict()
    for inp in inputs:
        tile_id, tile = inp.split("\n", 1)
        tile_id = int(tile_id[5:-1])
        tiles[tile_id] = tile.strip().split("\n")

    counts = defaultdict(int)
    for tile_id, tile in tiles.items():
        for t in gen(tile):
            for e in get_edges(t):
                counts[e] += 1
    ans1 = 1
    corners = []
    for tile_id, tile in tiles.items():
        ok = False
        for t in gen(tile):
            cnt = 0
            for e in get_edges(t):
                if counts[e] == 4:
                    cnt += 1
            if cnt == 2:
                ok = True
        if ok:
            corners.append(tile_id)
            ans1 *= tile_id

    print("Corners: ", corners)
    ctx.submit(1, ans1)

    side_len = 0
    while side_len * side_len < len(tiles):
        side_len += 1
    assert side_len*side_len == len(tiles)
    
    grid = None
    for t in gen(tiles[corners[0]]):
        grid = try_build_grid(t, tiles, corners)
        if grid is not None:
            break
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = trim_edges(grid[i][j])
    grid = join_grid(grid)
    
    pattern = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]

    ans2 = None
    for g in gen(grid):
        x = try_find(g, pattern)
        if x is not None:
            ans2 = x
    ctx.submit(2, ans2)
