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

arr = []
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        continue
    arr.append(int(line))


@timed("Part 1")
def part1():
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == 2020:
                return arr[i]*arr[j]
    raise Exception("Not found")


@timed("Part 2")
def part2():
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 2020:
                    return arr[i]*arr[j]*arr[k]
    raise Exception("Not found")

part1()
part2()