from puzzle import PuzzleContext
from collections import defaultdict


with PuzzleContext(year=2020, day=10) as ctx:
    ans1 = None
    ans2 = None

    # Part 1
    arr = [int(x) for x in ctx.nonempty_lines]
    arr.append(0)
    arr.append(max(arr) + 3)

    nums = sorted(arr)
    diffs = [b - a for a, b in zip(nums, nums[1:])]
    ans1 = diffs.count(1) * diffs.count(3)
    ctx.submit(1, ans1)

    # Part 2
    dp = defaultdict(int)
    dp[0] = 1
    for x in nums:
        for d in range(1, 3+1):
            y = x + d
            if y in nums:
                dp[y] += dp[x]
    ans2 = dp[max(nums)]

    ctx.submit(2, ans2)
