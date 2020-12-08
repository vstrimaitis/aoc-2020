import time
from puzzle import PuzzleContext
from interpreter import Program
from printer import Printer

printer = Printer() 
def print_progress(p: Program):
    printer.clear()
    printer.print(p)
    time.sleep(0.1)

with PuzzleContext(year=2020, day=8) as ctx:
    ans1 = None
    ans2 = None

    p = Program(ctx.data)
    p.run(cb=print_progress if ctx._is_running_on_sample() else None)
    printer.commit()
    ans1 = p.accumulator
    ctx.submit(1, ans1)

    lines = ctx.nonempty_lines
    for i in range(len(lines)):
        if "nop" in lines[i]:
            lines[i] = lines[i].replace("nop", "jmp")
            p = Program("\n".join(lines))
            p.run()
            if not p.stuck_in_loop:
                ans2 = p.accumulator
                break
            lines[i] = lines[i].replace("jmp", "nop")
        if "jmp" in lines[i]:
            lines[i] = lines[i].replace("jmp", "nop")
            p = Program("\n".join(lines))
            p.run()
            if not p.stuck_in_loop:
                ans2 = p.accumulator
                break
            lines[i] = lines[i].replace("nop", "jmp")
    ctx.submit(2, ans2)
