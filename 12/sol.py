from puzzle import PuzzleContext

def rotate_left(direction, amnt):
    if amnt == 0:
        return direction
    if direction == "N":
        return rotate_left("W", amnt-1)
    if direction == "W":
        return rotate_left("S", amnt-1)
    if direction == "S":
        return rotate_left("E", amnt-1)
    if direction == "E":
        return rotate_left("N", amnt-1)


def exec_action(action, cnt, x, y, d):
    if action == "N":
        return x, y + cnt, d
    if action == "S":
        return x, y - cnt, d
    if action == "E":
        return x + cnt, y, d
    if action == "W":
        return x - cnt, y, d
    if action == "L":
        if cnt % 90 != 0:
            raise ValueError
        cnt //= 90
        return x, y, rotate_left(d, cnt)
        
    if action == "R":
        if cnt % 90 != 0:
            raise ValueError
        cnt //= 90
        return x, y, rotate_left(d, 4-cnt)
    if action == "F":
        return exec_action(d, cnt, x, y, d)

def rotate_left_around(x, y, x0, y0, cnt):
    if cnt == 0:
        return x, y
    x -= x0
    y -= y0
    x, y = -y, x
    x += x0
    y += y0
    return rotate_left_around(x, y, x0, y0, cnt-1)

def exec_action2(action, cnt, x, y, d, wx, wy):
    if action in "NSEW":
        wx, wy, _ = exec_action(action, cnt, wx, wy, "")
        return x, y, d, wx, wy
    if action == "L":
        cnt //= 90
        wx, wy = rotate_left_around(wx, wy, x, y, cnt)
        return x, y, d, wx, wy
    if action == "R":
        cnt //= 90
        wx, wy = rotate_left_around(wx, wy, x, y, 4-cnt)
        return x, y, d, wx, wy

    if action == "F":
        dx = (wx-x)*cnt
        dy = (wy-y)*cnt
        x += dx
        y += dy
        wx += dx
        wy += dy
        return x, y, d, wx, wy


with PuzzleContext(year=2020, day=12) as ctx:
    ans1 = None
    ans2 = None

    curr_dir = "E"
    x = 0
    y = 0
    for line in ctx.nonempty_lines:
        action, cnt = line[0], int(line[1:])
        x, y, curr_dir = exec_action(action, cnt, x, y, curr_dir)

    ans1 = abs(x) + abs(y)

    wx = 10
    wy = 1
    x = 0
    y = 0
    curr_dir = "E"
    for line in ctx.nonempty_lines:
        action, cnt = line[0], int(line[1:])
        x, y, curr_dir, wx, wy = exec_action2(action, cnt, x, y, curr_dir, wx, wy)
            
    ans2 = abs(x) + abs(y)

    ctx.submit(1, ans1)
    ctx.submit(2, ans2)
