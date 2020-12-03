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
    return


@timed("Part 1")
def part1(data):
    return


@timed("Part 2")
def part2(data):
    return

INPUT = read()
part1(INPUT)
part2(INPUT)