from puzzle import PuzzleContext

def eval_op(op, x, y):
    if op == "+":
        return x+y
    return x * y

def to_rpn(expr, op_precs):
    output = []
    ops = []
    for i in range(len(expr)):
        token = expr[i]
        if token == " ":
            continue
        if token in "0123456789":
            output.append(int(token))
        elif token in op_precs.keys():
            while len(ops) > 0 and op_precs.get(ops[-1], 1e9) >= op_precs.get(token, 1e9) and ops[-1] != "(":
                output.append(ops.pop())
            ops.append(token)
        elif token == "(":
            ops.append(token)
        elif token == ")":
            while ops[-1] != "(":
                output.append(ops.pop())
            ops.pop()
    while len(ops) > 0:
        output.append(ops.pop())
    return output

def eval_rpn(rpn):
    stack = []
    for c in rpn:
        if isinstance(c, int):
            stack.append(c)
        else:
            x = stack.pop()
            y = stack.pop()
            stack.append(eval_op(c, x, y))
    return stack[0]

with PuzzleContext(year=2020, day=18) as ctx:

    lines = ctx.nonempty_lines
    
    ans1 = 0
    ans2 = 0
    OPS1 = {
        "+": 1,
        "*": 1
    }
    OPS2 = {
        "+": 2,
        "*": 1
    }
    for line in lines:
        rpn1 = to_rpn(line, OPS1)
        rpn2 = to_rpn(line, OPS2)
        
        ans1 += eval_rpn(rpn1)
        ans2 += eval_rpn(rpn2)
    ctx.submit(1, ans1)
    ctx.submit(2, ans2)
