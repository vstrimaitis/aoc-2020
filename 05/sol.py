from puzzle import PuzzleContext

def get_id(s):
    return int("".join(["0" if x in "FL" else "1" for x in s]), 2) 

with PuzzleContext(year=2020, day=5) as ctx:
    ids = []
    for l in ctx.data.split("\n"):
        ids.append(get_id(l))
    ctx.submit(1, max(ids))

    all_nums = set(range(min(ids), max(ids)+1))
    my_id = list(all_nums - set(ids))
    my_id = my_id[0]
    ctx.submit(2, my_id)
