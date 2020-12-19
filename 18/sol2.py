from puzzle import PuzzleContext
import ast

def evaluate(expr):
    root = ast.parse(expr, mode="eval")
    for node in ast.walk(root):
        if type(node) == ast.BinOp:
            node.op = ast.Add() if type(node.op) is ast.Div else ast.Mult()
    return eval(compile(root, "<string>", "eval"))

with PuzzleContext(year=2020, day=18) as ctx:

    lines = ctx.nonempty_lines
    ctx.submit(1, sum(evaluate(l.replace("+", "/")) for l in lines))
    ctx.submit(2, sum(evaluate(l.replace("+", "/").replace("*", "+")) for l in lines))
