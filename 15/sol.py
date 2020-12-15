from puzzle import PuzzleContext
from collections import defaultdict

def solve(nums, amnt):
    whens = defaultdict(list)
    for i, x in enumerate(nums):
        whens[x] = i

    nxt = 0
    for i in range(len(nums), amnt-1):
        x = 0 if nxt not in whens else i-whens[nxt]
        whens[nxt] = i
        nxt = x
    return nxt

with PuzzleContext(year=2020, day=15) as ctx:
    nums = [int(x) for x in ctx.lines[0].split(",")]

    ctx.submit(1, solve(nums, 2020))
    ctx.submit(2, solve(nums, 30000000))
