from puzzle import PuzzleContext


def calc1(group):
    d = dict()
    for g in group.split("\n"):
        for x in g.strip():
            if x not in d:
                d[x] = True
    # print(group, d)
    return len(d)


def calc2(group):
    d = dict()
    group = group.strip()
    num_groups = len(group.split("\n"))
    for g in group.split("\n"):
        for x in g.strip():
            if x not in d:
                d[x] = 0
            d[x] += 1
    ans = 0
    for k, v in d.items():
        if v == num_groups:
            ans += 1
    # print(group, d)
    return ans

with PuzzleContext(year=2020, day=6) as ctx:
    ans1 = None
    ans2 = None

    groups = ctx.data.split("\n\n")
    answers = [calc1(g) for g in groups]
    ans1 = sum(answers)
    # print(answers)

    ctx.submit(1, ans1)

    answers = [calc2(g) for g in groups]
    ans2 = sum(answers)
    # print(answers)
    ctx.submit(2, ans2)
