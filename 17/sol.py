from puzzle import PuzzleContext
import itertools

def get_neigh_coords(coord):
    c = []
    deltas = list(itertools.product([-1, 0, 1], repeat=len(coord)))
    for delta in deltas:
        if all(i == 0 for i in delta):
            continue
        new_c = tuple([x+dx for x, dx in zip(coord, delta)])
        c.append(new_c)
    return c

def get_neighs(space, coord):
    neighs = []
    for c in get_neigh_coords(coord):
        if c not in space:
            neighs.append(".")
        else:
            neighs.append(space[c])
    return neighs


def calc_next(space, coord):
    neighs = get_neighs(space, coord)
    if coord in space and space[coord] == "#":
        if neighs.count("#") == 2 or neighs.count("#") == 3:
            return "#"
        return "."

    if neighs.count("#") == 3:
        return"#"
    return "."


def simulate(space):
    new_space = space.copy()

    for c in space:
        for nc in get_neigh_coords(c):
            if nc not in new_space:
                new_space[nc] = "."

    for c in new_space:
        new_space[c] = calc_next(space, c)

    return new_space

def print_slice(space, z):
    slice = dict()
    min_i = None
    max_i = None
    min_j = None
    max_j = None
    for (zz, i, j) in space:
        if zz == z:
            slice[(i, j)] = space[(z, i, j)]
            if min_i is None:
                min_i = i
            if max_i is None:
                max_i = i
            if min_j is None:
                min_j = j
            if max_j is None:
                max_j = j

            min_i = min(min_i, i)
            max_i = max(max_i, i)
            min_j = min(min_j, j)
            max_j = max(max_j, j)

    for i in range(min_i, max_i+1):
        for j in range(min_j, max_j+1):
            print(space[(z, i, j)], end="")
        print()

def print_space(space, header=None):
    if header is not None:
        print(header)
    zs = set([z for z, _, _ in space.keys()])
    for z in sorted(zs):
        print(f"z = {z}")
        print_slice(space, z)
        print()
    print()

with PuzzleContext(year=2020, day=17) as ctx:
    # Part 1
    space = dict()
    for i, r in enumerate(ctx.nonempty_lines):
        for j, c in enumerate(r):
            space[(0, i, j)] = c
    # print_space(space, header="Before any cycles:")
    for i in range(6):
        space = simulate(space)
        # print_space(space, header=f"After {i+1} cycles:")
    ctx.submit(1, list(space.values()).count("#"))
    
    # Part 2
    space = dict()
    for i, r in enumerate(ctx.nonempty_lines):
        for j, c in enumerate(r):
            space[(0, 0, i, j)] = c
    for i in range(6):
        space = simulate(space)
    ctx.submit(2, list(space.values()).count("#"))
