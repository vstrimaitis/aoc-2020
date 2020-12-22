from puzzle import PuzzleContext

def encode_deck(d):
    return ",".join(str(x) for x in d)

def encode(d1, d2):
    return encode_deck(d1) + "|" + encode_deck(d2)

def calc_score(p):
    ans = 0
    for i, x in enumerate(reversed(p)):
        ans += (i+1) * x
    return ans

def rec(p1, p2, cache, tab=0):
    p1 = p1.copy()
    p2 = p2.copy()
    seen = set()
    while len(p1) > 0 and len(p2) > 0:
        key = encode(p1, p2)
        if key in seen:
            return p1, p2, 1
        seen.add(key)
        c1, p1 = p1[0], p1[1:]
        c2, p2 = p2[0], p2[1:]
        if len(p1) >= c1 and len(p2) >= c2:
            _, _, win = rec(p1[:c1], p2[:c2], cache, tab+1)
            if win == 1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        elif c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    if len(p1) == 0:
        return p1, p2, 2
    return p1, p2, 1

with PuzzleContext(year=2020, day=22) as ctx:

    players = [[int(y) for y in x.split("\n")[1:]] for x in ctx.data.split("\n\n")]
    while all(len(p) > 0 for p in players):
        c1, c2 = players[0][0], players[1][0]
        players = [players[0][1:], players[1][1:]]
        if c1 > c2:
            players[0].extend([c1, c2])
        else:
            players[1].extend([c2, c1])

    scores = [calc_score(p) for p in players]
    ctx.submit(1, max(scores))

    [p1, p2] = [[int(y) for y in x.split("\n")[1:]] for x in ctx.data.split("\n\n")]
    p1, p2, win = rec(p1, p2, dict())
    # print(p1, p2, win)
    score1 = calc_score(p1)
    score2 = calc_score(p2)
    ctx.submit(2, max(score1, score2))
