from puzzle import PuzzleContext


def match(message, r_defs, r_id):
    rule = r_defs[r_id]
    if '"' in rule:
        letter = rule[1]
        if message and message[0] == letter:
            yield message[1:]
        return

    def gen(r_ids, m, k=0):
        if k == len(r_ids):
            yield m
            return
        for new_m in match(m, r_defs, int(r_ids[k])):
            for x in gen(r_ids, new_m, k + 1):
                yield x

    parts = rule.split(" | ")
    for part in parts:
        m = message
        r_ids = part.split(" ")
        for x in gen(r_ids, m):
            yield x
    return None


def solve(rules, queries):
    defs = dict()
    for line in rules:
        [r_id, r_def] = line.split(": ")
        defs[int(r_id)] = r_def

    ans = 0
    for q in queries:
        ok = False
        for x in match(q, defs, 0):
            if x == "":
                ok = True
                break
        if ok:
            ans += 1
    return ans


with PuzzleContext(year=2020, day=19) as ctx:
    defs, queries = ctx.data.split("\n\n")

    queries = queries.split("\n")
    ctx.submit(1, solve(defs.split("\n"), queries))
    # insight from the data: only rule 0 depends on rules 8 and 11;
    # 8 and 11 are the only looping ones
    ctx.submit(
        2,
        solve(
            defs.replace("8: 42", "8: 42 | 42 8")
            .replace("11: 42 31", "11: 42 31 | 42 11 31")
            .split("\n"),
            queries,
        ),
    )
