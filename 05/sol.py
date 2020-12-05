from puzzle import PuzzleContext
import re

with PuzzleContext(year=2020, day=5) as ctx:
    ids = []
    for l in ctx.data.split("\n"):
        l = re.sub(r"[FL]", "0", l)
        l = re.sub(r"[BR]", "1", l)
        ids.append(int(l, 2))
    ctx.submit(1, max(ids))

    all_nums = set(range(min(ids), max(ids)+1))
    my_id = list(all_nums - set(ids))
    my_id = my_id[0]
    ctx.submit(2, my_id)
