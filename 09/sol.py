from puzzle import PuzzleContext

def can_be_made(window, x):
    for y in window:
        z = x-y
        if z in window:
            return True
    return False

with PuzzleContext(year=2020, day=9) as ctx:
    ans1 = None
    ans2 = None

    SZ = 25
    data = [int(x) for x in ctx.nonempty_lines]
    window = data[:SZ]
    for i in range(SZ, len(data)):
        x = data[i]
        if not can_be_made(window, x):
            ans1 = x
            break
        window = window[1:]
        window.append(x)

    ctx.submit(1, ans1)

    psums = [0]
    d = dict()
    d[0] = 0
    for x in data:
        psums.append(psums[-1] + x)
        d[psums[-1]] = len(psums)-1

    for i in range(len(data)):
        need = psums[i+1] - ans1
        if need in d:
            j = d[need]
            ans2 = min(data[j:i+1]) + max(data[j:i+1])
            break
    # Stupid solution that would have worked but I decided to write a more efficient one :(
    # for i in range(len(data)):
    #     s = 0
    #     for j in range(i, len(data)):
    #         s += data[j]
    #         if s > ans1:
    #             break
    #         if s == ans1 and j > i:
    #             ans2 = min(data[i:j+1]) + max(data[i:j+1])
    #             break
    ctx.submit(2, ans2)
