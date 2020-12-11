from puzzle import PuzzleContext

DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def count(brd, i, j, c):
    n = len(brd)
    m = len(brd[0])
    cnt = 0
    for di, dj in DIRS:
        ii = di + i
        jj = dj + j
        if ii == i and jj == j:
            continue
        if ii >= 0 and ii < n and jj >= 0 and jj < m and brd[ii][jj] == c:
            cnt += 1
    return cnt


def count2(brd, i, j, c):
    n = len(brd)
    m = len(brd[0])
    cnt = 0

    for di, dj in DIRS:
        ii = i + di
        jj = j + dj
        while ii >= 0 and ii < n and jj >= 0 and jj < m:
            if brd[ii][jj] != ".":
                if brd[ii][jj] == c:
                    cnt += 1
                break
            ii += di
            jj += dj

    return cnt



def simulate(brd):
    new_brd = [[c for c in r] for r in brd]
    n = len(brd)
    m = len(brd[0])
    changed = False
    for i in range(n):
        for j in range(m):
            if brd[i][j] == ".":
                continue
            cnt_empty = count(brd, i, j, "L")
            cnt_occ = count(brd, i, j, "#")
            if brd[i][j] == "L" and cnt_occ == 0:
                new_brd[i][j] = "#"
                changed = True
            if brd[i][j] == "#" and cnt_occ >= 4:
                new_brd[i][j] = "L"
                changed = True
        
    new_brd = ["".join(r) for r in new_brd]
    return new_brd, changed

def simulate2(brd):
    new_brd = [[c for c in r] for r in brd]
    n = len(brd)
    m = len(brd[0])
    changed = False
    for i in range(n):
        for j in range(m):
            if brd[i][j] == ".":
                continue
            cnt_empty = count2(brd, i, j, "L")
            cnt_occ = count2(brd, i, j, "#")
            if brd[i][j] == "L" and cnt_occ == 0:
                new_brd[i][j] = "#"
                changed = True
            if brd[i][j] == "#" and cnt_occ >= 5:
                new_brd[i][j] = "L"
                changed = True
        
    new_brd = ["".join(r) for r in new_brd]
    return new_brd, changed


with PuzzleContext(year=2020, day=11) as ctx:
    ans1 = None
    ans2 = None

    brd = ctx.nonempty_lines

    while True:
        brd, changed = simulate(brd)
        if not changed:
            break

    ans1 = "".join(brd).count("#")

    ctx.submit(1, ans1)


    brd = ctx.nonempty_lines
    while True:
        brd, changed = simulate2(brd)
        if not changed:
            break

    ans2 = "".join(brd).count("#")

    ctx.submit(2, ans2)
