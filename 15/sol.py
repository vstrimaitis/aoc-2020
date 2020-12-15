from puzzle import PuzzleContext
from collections import defaultdict

def exec_iteration(nums, whens, i):
    x = nums[-1]
    if len(whens[x]) == 1:
        speak = 0
    else:
        speak = whens[x][-1] - whens[x][-2]

    whens[speak].append(i)
    nums.append(speak)

with PuzzleContext(year=2020, day=15) as ctx:
    nums = [int(x) for x in ctx.lines[0].split(",")]

    whens = defaultdict(list) # spoken number -> list of times when spoken
    for i, x in enumerate(nums):
        whens[x] = [i]

    for i in range(len(nums), 2020):
        exec_iteration(nums, whens, i)
    ctx.submit(1, nums[-1])

    for i in range(len(nums), 30000000):
        exec_iteration(nums, whens, i)
    ctx.submit(2, nums[-1])
