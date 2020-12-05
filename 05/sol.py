from puzzle import PuzzleContext

def calc(n, sides):
    lo = 0
    hi = n-1
    for c in sides:
        mid = (lo+hi)//2
        if c == "L":
            hi = mid
        else:
            lo = mid+1
    return lo

def get_id(s):
    fb = s[:7]
    lr = s[7:]
    row = calc(128, ["L" if x == "F" else "B" for x in fb])
    col = calc(8, lr)
    return row*8+col

with PuzzleContext(year=2020, day=5) as ctx:
    ids = []
    for l in ctx.data.split("\n"):
        ids.append(get_id(l))
    ctx.submit(1, max(ids))

    my_id = -1
    ids = sorted(ids)
    for i in range(len(ids)-1):
        if ids[i+1] != ids[i]+1:
            my_id = ids[i]+1
            break
    ctx.submit(2, my_id)
