from puzzle import PuzzleContext


def move_1_to_front(cups):
    idx = cups.index(1)
    return cups[idx:] + cups[:idx]

def do_move(cups, curr):
    n = len(cups)
    curr_val = cups[curr]
    picked = [cups[(curr+1)%n], cups[(curr+2)%n], cups[(curr+3)%n]]
    cups = [x for x in cups if x not in picked]
        
    dest_val = curr_val - 1
    vals = set(cups)
    while True:
        if dest_val in vals:
            dest_idx = cups.index(dest_val)
            break
        else:
            dest_val -= 1
            if dest_val < min(cups):
                dest_val = max(cups)

    cups = cups[:dest_idx+1] + picked + cups[dest_idx+1:]
    cups = move_1_to_front(cups)
    curr = cups.index(curr_val)
    curr = (curr + 1) % n
    return cups, curr

def simulate(cups, iters):
    nxt = dict()
    prev = cups[-1]
    for x in cups:
        nxt[prev] = x
        prev = x
    curr = cups[0]
    mx = max(cups)
    mn = min(cups)

    for _ in range(iters):
        a = nxt[curr]
        b = nxt[a]
        c = nxt[b]
        after = nxt[c]

        nxt[curr] = after
        dest = curr
        while True:
            dest -= 1
            if dest < mn:
                dest = mx
            if dest not in (a, b, c):
                break
        nxt[c] = nxt[dest]
        nxt[dest] = a
        curr = after
    res = [1]
    while nxt[res[-1]] != 1:
        res.append(nxt[res[-1]])
    return res

with PuzzleContext(year=2020, day=23) as ctx:
    cups = [int(x) for x in list(ctx.data.strip())]
    cups = simulate(cups, 100)
    ctx.submit(1, "".join(str(x) for x in cups[1:]))

    cups = [int(x) for x in list(ctx.data.strip())]
    while len(cups) < 1000000:
        cups.append(len(cups)+1)
    cups = simulate(cups, 10000000)
    ctx.submit(2, cups[1]*cups[2])
