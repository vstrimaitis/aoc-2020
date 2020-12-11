from puzzle import PuzzleContext

DIRS = [
    (i, j)
    for i in [-1, 0, 1]
    for j in [-1, 0, 1]
    if not (i == 0 and j == 0)
]

def is_inside(brd, i, j):
    n = len(brd)
    m = len(brd[0])
    return i >= 0 and i < n and j >= 0 and j < m 

def count_adjacent(brd, i, j, c):
    cnt = 0
    for di, dj in DIRS:
        ii = di + i
        jj = dj + j
        if is_inside(brd, ii, jj) and brd[ii][jj] == c:
            cnt += 1
    return cnt


def count_visible(brd, i, j, c):
    cnt = 0

    for di, dj in DIRS:
        ii = i + di
        jj = j + dj
        while is_inside(brd, ii, jj):
            if brd[ii][jj] != ".":
                if brd[ii][jj] == c:
                    cnt += 1
                break
            ii += di
            jj += dj

    return cnt


def simulate(brd, count_neighs, rules):
    new_brd = [[c for c in r] for r in brd]
    n = len(brd)
    m = len(brd[0])
    for i in range(n):
        for j in range(m):
            n_occupied = count_neighs(brd, i, j, "#")
            new_brd[i][j] = rules[brd[i][j]](n_occupied)

    new_brd = ["".join(r) for r in new_brd]
    changed = brd != new_brd
    return new_brd, changed


with PuzzleContext(year=2020, day=11) as ctx:
    # Part 1
    brd = ctx.nonempty_lines
    while True:
        brd, changed = simulate(brd, count_adjacent, rules={
            "L": lambda n_occupied: "#" if n_occupied == 0 else "L",
            "#": lambda n_occupied: "L" if n_occupied >= 4 else "#",
            ".": lambda _: ".",
        })
        if not changed:
            break

    ctx.submit(1, "".join(brd).count("#"))

    # Part 2
    brd = ctx.nonempty_lines
    while True:
        brd, changed = simulate(brd, count_visible, rules={
            "L": lambda n_occupied: "#" if n_occupied == 0 else "L",
            "#": lambda n_occupied: "L" if n_occupied >= 5 else "#",
            ".": lambda _: ".",
        })
        if not changed:
            break

    ctx.submit(2, "".join(brd).count("#"))
