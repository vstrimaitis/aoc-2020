from puzzle import PuzzleContext


with PuzzleContext(year=2020, day=10) as ctx:
    ans1 = None
    ans2 = None

    nums = set(int(x) for x in ctx.nonempty_lines)

    curr = 0
    mx = max(nums) + 3
    cnts = dict()
    cnts[1] = 0
    cnts[2] = 0
    cnts[3] = 0
    nums.add(mx)
    while True:
        found = False
        for d in range(1, 3+1):
            if curr + d in nums:
                curr += d
                cnts[d] += 1
                found = True
                break
        if not found:
            break
    ans1 = cnts[1] * cnts[3]

    nums.add(0)
    nums = list(nums)
    dp = dict()
    dp[0] = 1
    for x in nums:
        for d in range(1, 3+1):
            y = x + d
            if y in nums:
                if y not in dp:
                    dp[y] = 0
                dp[y] += dp[x]
    ans2 = dp[mx]

    ctx.submit(1, ans1)
    ctx.submit(2, ans2)
