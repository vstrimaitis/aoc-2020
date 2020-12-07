from puzzle import PuzzleContext

def parse_line(l):
    l = l[:-1]
    parts = l.split(" contain ")
    big = parts[0][:-1] # remove "s" suffix]
    if parts[1] == "no other bags":
        return big, []
    parts = parts[1].split(", ")
    arr = []
    for p in parts:
        cnt, name = int(p.split(" ")[0]), " ".join(p.split(" ")[1:])
        if cnt > 1:
            name = name[:-1]
        arr.append((cnt, name))
    return big, arr

def dfs(adj, u, visited):
    visited.add(u)
    for v in adj[u]:
        if v not in visited:
            dfs(adj, v, visited)


def dfs2(adj, u, dp):
    if u in dp:
        return dp[u]
    dp[u] = 1
    for v, cnt in adj[u]:
        if v not in visited:
            dp[u] += cnt * dfs2(adj, v, dp)
    return dp[u]
    


with PuzzleContext(year=2020, day=7) as ctx:
    ans1 = None
    ans2 = None

    adj = dict()
    rev_adj = dict()

    for line in ctx.nonempty_lines:
        main, others = parse_line(line)
        if main not in adj:
            adj[main] = []
        for cnt, other in others:
            adj[main].append((other, cnt))
            if other not in adj:
                adj[other] = []

        if main not in rev_adj:
            rev_adj[main] = []
        for cnt, other in others:
            if other not in rev_adj:
                rev_adj[other] = []
            rev_adj[other].append(main)
    
    visited = set()
    dfs(rev_adj, "shiny gold bag", visited)
    visited.remove("shiny gold bag")
    ans1 = len(visited)

    dp = dict()
    dfs2(adj, "shiny gold bag", dp)
    ans2 = dp["shiny gold bag"] - 1  # remove starting bag

    ctx.submit(1, ans1)
    ctx.submit(2, ans2)
