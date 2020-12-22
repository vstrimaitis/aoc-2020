from puzzle import PuzzleContext

def encode_deck(d):
    return ",".join(str(x) for x in d)

def encode(players):
    return "|".join(encode_deck(p) for p in players)

def calc_score(p):
    ans = 0
    for i, x in enumerate(reversed(p)):
        ans += (i+1) * x
    return ans

def rec(players, cache, tab=0):
    seen = set()
    while all(len(p) > 0 for p in players):
        key = encode(players)
        if key in seen:
            return players, 0
        seen.add(key)
        cs = [p[0] for p in players]
        players = [p[1:] for p in players]
        if all(len(p) >= c for p, c in zip(players, cs)):
            next_players = [p[:c] for p, c in zip(players, cs)]
            _, win = rec(next_players, cache, tab+1)
            if win != 0:
                cs = reversed(cs)
            players[win].extend(cs)
        elif cs[0] > cs[1]:
            players[0].extend(cs)
        else:
            players[1].extend(reversed(cs))
    return players, 1 if len(players[0]) == 0 else 0

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

    players = [[int(y) for y in x.split("\n")[1:]] for x in ctx.data.split("\n\n")]
    players, win = rec(players, dict())
    scores = [calc_score(p) for p in players]
    ctx.submit(2, max(scores))
