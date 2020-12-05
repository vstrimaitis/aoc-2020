from puzzle import PuzzleContext

def get_id(s):
    return int("".join(["0" if x in "FL" else "1" for x in s]), 2) 

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
