from puzzle import PuzzleContext
import math

def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = ext_gcd(b, a%b)
    x = y1
    y = x1 - y1 * (a // b)

    return d, x, y

with PuzzleContext(year=2020, day=13) as ctx:
    ans1 = None
    ans2 = None

    # Part 1
    ts = int(ctx.nonempty_lines[0])
    bus_ids = [int(x) for x in ctx.nonempty_lines[1].split(",") if x != "x"]

    nexts = [math.ceil(ts / bus_id)*bus_id for bus_id in bus_ids]
    min_next = min(nexts)
    best_bus_id = bus_ids[nexts.index(min_next)]
    min_wait = min_next - ts
    ctx.submit(1, min_wait * best_bus_id)

    # Part 2
    bus_ids = [(None if x == "x" else int(x)) for x in ctx.nonempty_lines[1].split(",")]
    for i in range(len(bus_ids)):
        if bus_ids[i] is not None:
            bus_ids[i] = (bus_ids[i], i)
    bus_ids = [x for x in bus_ids if x is not None]

    # need to solve this system of congruences:
    # x % id[0] == 0
    # x % id[1] == -1
    # x % id[2] == -2
    # x % id[3] == -3
    # ...
    congruences = []
    for bid, i in bus_ids:
        congruences.append((-i, bid))
    while len(congruences) > 1:
        a1, n1 = congruences.pop()
        a2, n2 = congruences.pop()
        # solve m1*n1 + m2*n2 = 1
        g, m1, m2 = ext_gcd(n1, n2)
        x = a1*m2*n2 + a2*m1*n1
        print(f"{n1}*m1 + {n2}*m2 = {g} => m1={m1}, m2={m2}, x={x}")
        congruences.append((x, n1*n2))

    ctx.submit(2, congruences[0][0] % congruences[0][1])
