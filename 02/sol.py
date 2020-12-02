import sys

def is_valid_1(times, char, pwd):
    cnt = 0
    for c in pwd:
        if c == char:
            cnt += 1
    return times[0] <= cnt and cnt <= times[1]

def is_valid_2(times, char, pwd):
    a = pwd[times[0]-1] == char
    b = pwd[times[1]-1] == char
    return a ^ b

pwds = []
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        continue
    parts = line.split(": ")
    p1 = parts[0].split(" ")
    times = [int(x) for x in p1[0].split("-")]
    char = p1[1]
    pwd = parts[1]

    pwds.append((times, char, pwd))


def part1():
    ans = 0
    for (times, char, pwd) in pwds:
        if is_valid_1(times, char, pwd):
            ans += 1
    print("Part 1: ", ans)

def part2():
    ans = 0
    for (times, char, pwd) in pwds:
        if is_valid_2(times, char, pwd):
            ans += 1
    print("Part 1: ", ans)

part1()
part2()