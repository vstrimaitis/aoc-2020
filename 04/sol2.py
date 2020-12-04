from puzzle import PuzzleContext
from passport import from_input


with PuzzleContext(year=2020, day=4) as ctx:
    p1 = from_input(ctx.data, run_validators=False)
    p1 = len(p1)
    ctx.submit(1, p1)

    p2 = from_input(ctx.data, run_validators=True)
    p2 = len(p2)
    ctx.submit(2, p2)
