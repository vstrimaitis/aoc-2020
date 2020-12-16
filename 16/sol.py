from puzzle import PuzzleContext


def valid_for_any(ranges, val):
    for t in ranges:
        for r in ranges[t]:
            [lo, hi] = r
            if lo <= val <= hi:
                return True
    return False

with PuzzleContext(year=2020, day=16) as ctx:
    ans1 = None
    ans2 = None

    parts = ctx.data.split("\n\n")
    my_ticket = None
    tickets = []
    ranges = dict()
    for part in parts:
        p = part.split("\n")
        header, vals = p[0], p[1:]
        if "your ticket" in header:
            my_ticket = [int(x) for x in vals[0].split(",")]
        elif "nearby tickets" in header:
            for v in vals:
                if not v:
                    continue
                tickets.append([int(x) for x in v.split(",")])
        else:
            for x in p:
                name, val = x.split(": ")[0], x.split(": ")[1]
                rs = val.split(" or ")
                rs = [[int(x) for x in r.split("-")] for r in rs]
                ranges[name] = rs

    ans1 = 0
    valid_tickets = []
    for ticket in tickets:
        is_valid = True
        for val in ticket:
            if not valid_for_any(ranges, val):
                ans1 += val
                is_valid = False
        if is_valid:
            valid_tickets.append(ticket)

    ctx.submit(1, ans1)

    valid_tickets.append(my_ticket)
    valid_types = []
    for ticket in valid_tickets:
        valid_types_per_pos = []
        for val in ticket:
            v = set()
            for t in ranges:
                found = False
                for r in ranges[t]:
                    if r[0] <= val <= r[1]:
                        found = True
                if found:
                    v.add(t)
            valid_types_per_pos.append(v)
        valid_types.append(valid_types_per_pos)
        
    # intersect valid types per column
    reduced = []
    for i in range(len(valid_tickets[0])):
        poss = None
        for j in range(len(valid_tickets)):
            if poss is None:
                poss = valid_types[j][i]
            else:
                poss &= valid_types[j][i]
        reduced.append(poss)

    # take valid types per column with only one possibility at a time
    # remove that possibility from all other cols
    finished = [False] * len(reduced)
    for i in range(len(tickets[0])):
        take = None
        for j in range(len(reduced)):
            if len(reduced[j]) == 1 and not finished[j]:
                take = j
                break
        finished[take] = True
        for j in range(len(reduced)):
            if j != take:
                reduced[j] -= reduced[take]

    ans2 = 1        
    for j in range(len(reduced)):
        assert len(reduced[j]) == 1
        label = list(reduced[j])[0]
        if "departure" in label:
            print(j, label, my_ticket, my_ticket[j])
            ans2 *= my_ticket[j]
    
    ctx.submit(2, ans2)
