from puzzle import PuzzleContext

def exec_prog(prog):
    ip = 0
    seen = set()
    acc = 0

    while True:
        if ip >= len(prog):
            break
        op, arg = prog[ip].split()
        if ip in seen:
            return True, acc
        seen.add(ip)
        arg = int(arg)
        if op == "nop":
            ip += 1
            continue
        if op == "acc":
            acc += arg
            ip += 1
            continue
        if op == "jmp":
            ip += arg
            continue
    return False, acc
    

with PuzzleContext(year=2020, day=8) as ctx:
    ans1 = None
    ans2 = None
    
    lines = ctx.nonempty_lines
    _, ans1 = exec_prog(lines)

    for i in range(len(lines)):
        if "nop" in lines[i]:
            l = lines[i]
            lines[i] = lines[i].replace("nop", "jmp")
            looped, acc = exec_prog(lines)
            lines[i] = l

            if not looped:
                ans2 = acc
                break
        if "jmp" in lines[i]:
            l = lines[i]
            lines[i] = lines[i].replace("jmp", "nop")
            looped, acc = exec_prog(lines)
            lines[i] = l

            if not looped:
                ans2 = acc
                break

    ctx.submit(1, ans1)
    ctx.submit(2, ans2)
