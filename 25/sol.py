from puzzle import PuzzleContext
import math

def discrete_log(a, b, p):
    # Finds x such that log_a(x) = b mod p
    n = 1 + int(math.sqrt(p))
    baby_steps = {}
    baby_step = 1
    for r in range(n+1):
        baby_steps[baby_step] = r
        baby_step = baby_step * a % p

    giant_stride = pow(a,(p-2)*n,p)
    giant_step = b
    for q in range(n+1):
        if giant_step in baby_steps:
            return q*n + baby_steps[giant_step]
        else:
            giant_step = giant_step * giant_stride % p
    return None


with PuzzleContext(year=2020, day=25) as ctx:
    MOD = 20201227
    card_pub, door_pub = [int(x) for x in ctx.nonempty_lines]
    card_loop = discrete_log(7, card_pub, MOD)
    door_loop = discrete_log(7, door_pub, MOD)

    print("card loop size", card_loop)
    print("door loop size", door_loop)

    assert card_pub == pow(7, card_loop, MOD)
    assert door_pub == pow(7, door_loop, MOD)

    encr_key = pow(card_pub, door_loop, MOD)
    assert encr_key == pow(door_pub, card_loop, MOD)

    ctx.submit(1, encr_key)
