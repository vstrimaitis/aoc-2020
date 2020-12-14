from puzzle import PuzzleContext
import re

def expand(x):
    if "X" not in x:
        return [x]
    res = []
    for i, c in enumerate(x):
        if c == "X":
            x0 = x[:i] + "0" + x[i+1:]
            x1 = x[:i] + "1" + x[i+1:]
            res.extend(expand(x0))
            res.extend(expand(x1))
            break
    return res

with PuzzleContext(year=2020, day=14) as ctx:
    ans1 = None
    ans2 = None

    prog = ctx.nonempty_lines

    mask = "X"*36
    mem = dict()
    for line in prog:
        m = re.match(r"mem\[(\d+)\] = (\d+)", line)
        if m:
            addr = int(m[1])
            val = bin(int(m[2]))[2:].rjust(36, "0")
            new_val = []
            for c1, c2 in zip(mask, val):
                if c1 == "X":
                    new_val.append(c2)
                else:
                    new_val.append(c1)
            new_val = "".join(new_val)
            mem[addr] = int(new_val, 2)
        m = re.match(r"mask = ([01X]+)", line)
        if m:
            mask = m[1]
    ctx.submit(1, sum(mem.values()))

    mem = dict()
    for line in prog:
        m = re.match(r"mask = ([01X]+)", line)
        if m:
            mask = m[1]
            continue
        m = re.match(r"mem\[(\d+)\] = (\d+)", line)
        addr = bin(int(m[1]))[2:].rjust(36, "0")
        val = int(m[2])
        new_addr = []
        for c1, c2 in zip(mask, addr):
            if c1 in "X1":
                new_addr.append(c1)
            elif c1 == "0":
                new_addr.append(c2)
        new_addr = "".join(new_addr)

        for addr in expand(new_addr):
            mem[int(addr, 2)] = val
    
    ctx.submit(2, sum(mem.values()))
