from puzzle import PuzzleContext
import re

def expand(x):
    if "X" not in x:
        return [x]
    x0 = x.replace("X", "0", 1)
    x1 = x.replace("X", "1", 1)
    return expand(x0) + expand(x1)

def parse_line(line):
    m = re.match(r"mask = ([01X]+)", line)
    if m:
        return "mask", [m[1]]
    m = re.match(r"mem\[(\d+)\] = (\d+)", line)
    if m:
        return "mem", [int(m[1]), int(m[2])]

def apply_mask(val, mask, subst_table):
    return "".join([subst_table[c1] or c2 for c1, c2 in zip(mask, val)])
    
with PuzzleContext(year=2020, day=14) as ctx:
    prog = ctx.nonempty_lines

    # Part 1
    mask = None
    mem = dict()
    for line in prog:
        op, args = parse_line(line)
        if op == "mask":
            mask = args[0]
        else:
            [addr, val] = args
            val = bin(val)[2:].rjust(36, "0")
            val = apply_mask(val, mask, {"X": None, "0": "0", "1": "1"})
            mem[addr] = int(val, 2)
    ctx.submit(1, sum(mem.values()))

    # Part 2
    mem = dict()
    for line in prog:
        op, args = parse_line(line)
        if op == "mask":
            mask = args[0]
        else:
            [addr, val] = args
            addr = bin(addr)[2:].rjust(36, "0")
            addr = apply_mask(addr, mask, {"X": "X", "1": "1", "0": None})
            for a in expand(addr):
                mem[int(a, 2)] = val
    ctx.submit(2, sum(mem.values()))
