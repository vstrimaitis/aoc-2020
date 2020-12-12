from puzzle import PuzzleContext
from collections import OrderedDict

DIRS = OrderedDict(
    N=(0, +1),
    W=(-1, 0),
    S=(0, -1),
    E=(+1, 0),
)

def rotate_left(direction, amnt):
    if amnt == 0:
        return direction
    directions = list(DIRS)
    i = directions.index(direction)
    i = (i + 1) % len(directions)
    return rotate_left(directions[i], amnt-1)


def exec_action(action, cnt, x, y, d):
    if action in DIRS.keys():
        dx, dy = DIRS[action]
        return x + dx*cnt, y + dy*cnt, d
    if action == "L":
        return x, y, rotate_left(d, cnt // 90)
    if action == "R":
        return x, y, rotate_left(d, 4 - cnt // 90)
    if action == "F":
        return exec_action(d, cnt, x, y, d)

def rotate_left_around_0(x, y, cnt):
    if cnt == 0:
        return x, y
    x, y = -y, x
    return rotate_left_around_0(x, y, cnt-1)

def exec_action_2(action, cnt, x, y, wx, wy):
    if action in DIRS.keys():
        wx, wy, _ = exec_action(action, cnt, wx, wy, "")
        return x, y, wx, wy
    if action == "L":
        wx, wy = rotate_left_around_0(wx, wy, cnt // 90)
        return x, y, wx, wy
    if action == "R":
        wx, wy = rotate_left_around_0(wx, wy, 4 - cnt // 90)
        return x, y, wx, wy
    if action == "F":
        return x + wx*cnt, y + wy*cnt, wx, wy


with PuzzleContext(year=2020, day=12) as ctx:
    actions = [(line[0], int(line[1:])) for line in ctx.nonempty_lines]
    
    # Part 1
    curr_dir = "E"
    x, y = 0, 0
    for action, cnt in actions:
        x, y, curr_dir = exec_action(action, cnt, x, y, curr_dir)
    ctx.submit(1, abs(x) + abs(y))

    # Part 2
    wx, wy = 10, 1  # relative to the ship
    x, y = 0, 0
    for action, cnt in actions:
        x, y, wx, wy = exec_action_2(action, cnt, x, y, wx, wy)   
    ctx.submit(2, abs(x) + abs(y))
