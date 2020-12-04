import sys
from passport import from_input

stdin = sys.stdin.read()

p1 = from_input(stdin, run_validators=False)
print("Part 1: ", len(p1))

p2 = from_input(stdin, run_validators=True)
print("Part 2: ", len(p2))
