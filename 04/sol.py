import sys
import time
import functools
import re

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
    p = dict()
    for line in sys.stdin.readlines():
        line = line.strip()
        if not line:
            arr.append(p)
            p = dict()
            continue
        for x in line.split(" "):
            p[x.split(":")[0]] = x.split(":")[1]
    arr.append(p)
    return arr

def valid_byr(s):
    return re.match("^\d{4}$", s) and 1920 <= int(s) <= 2002

def valid_iyr(s):
    return re.match("^\d{4}$", s) and 2010 <= int(s) <= 2020

def valid_eyr(s):
    return re.match("^\d{4}$", s) and 2020 <= int(s) <= 2030

def valid_hgt(s):
    x = re.search("^(\d+)(in|cm)$", s)
    if x is None:
        return False
    if x[2] == "cm":
        return 150 <= int(x[1]) <= 193
    return 59 <= int(x[1]) <= 76

def valid_hcl(s):
    return re.match("^#[0-9a-f]{6}$", s)

def valid_ecl(s):
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def valid_pid(s):
    return re.match("^\d{9}$", s)


def is_valid(p, include_validation, optional={"cid": None}, required={"byr": valid_byr, "iyr": valid_iyr, "eyr": valid_eyr, "hgt": valid_hgt, "hcl": valid_hcl, "ecl": valid_ecl, "pid": valid_pid}):
    for r in required:
        if r not in p:
            return False
        fn = required[r]
        if include_validation and fn is not None and not fn(p[r]):
            return False
    return True


@timed("Part 1")
def part1(data):
    ans = 0
    for p in data:
        if is_valid(p, include_validation=False):
            ans += 1
    return ans


@timed("Part 2")
def part2(data):
    ans = 0
    for p in data:
        if is_valid(p, include_validation=True):
            ans += 1
    return ans

INPUT = read()
part1(INPUT)
part2(INPUT)