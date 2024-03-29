import sys
import time
import functools

def timed(message=None):
    def inner(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            start = time.time()
            res = f(*args, **kwargs)
            end = time.time()

            sec = end-start
            if message is None:
                print(f"{res} ({sec} sec)")
            else:
                print(f"{message}: {res} ({sec} sec)")
            return res
        return wrapper
    return inner

def read():
    arr = []
    for line in sys.stdin.readlines():
        line = line.strip()
        if not line:
            continue
        arr.append(int(line))
    return arr


@timed("Part 1")
def part1(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i]*data[j]
    raise Exception("Not found")


@timed("Part 2")
def part2(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            for k in range(j+1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i]*data[j]*data[k]
    raise Exception("Not found")

INPUT = read()
part1(INPUT)
part2(INPUT)