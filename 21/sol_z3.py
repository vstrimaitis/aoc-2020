from puzzle import PuzzleContext
from collections import defaultdict
import z3



with PuzzleContext(year=2020, day=21) as ctx:
    allergen_to_food = defaultdict(set)
    ingredient_to_food = defaultdict(set)
    foods = []
    for i, line in enumerate(ctx.nonempty_lines):
        ingredients, allergens = line.split(" (")
        allergens = allergens[:-1].replace("contains ", "").split(", ")
        ingredients = ingredients.split(" ")
        foods.append((allergens, ingredients))
        for allergen in allergens:
            allergen_to_food[allergen].add(i)
        for ing in ingredients:
            ingredient_to_food[ing].add(i)

ok_ings = set()
ans1 = 0
for ing, i1 in ingredient_to_food.items():
    if not any(i2 < i1 for _, i2 in allergen_to_food.items()):
        ok_ings.add(ing)
        ans1 += len(ingredient_to_food[ing])
ctx.submit(1, ans1)

ings = list(set(ingredient_to_food.keys()) - ok_ings)
allergens = list(set(allergen_to_food.keys()))
assert len(ings) == len(allergens)

assignments = z3.IntVector("allergen", len(allergens))
solver = z3.Solver()
for a in assignments:
    # each assignment must map to an index in the `allergens` list
    solver.add(0 <= a)
    solver.add(a < len(allergens))
# all assignments must be distinct (i.e. no two assignments must map to the same ingredient)
solver.add(z3.Distinct(assignments))

for ai, allergen in enumerate(allergens):
    conds = []
    for ii, ing in enumerate(ings):
        # if food ids for the allergen is a subset of food ids for the ingredient
        if ingredient_to_food[ing] >= allergen_to_food[allergen]:
            conds.append(assignments[ii] == ai)
    solver.add(z3.Or(conds))
assert solver.check() == z3.sat
m = solver.model()
print(solver)
matches = []
for ii, a in enumerate(assignments):
    matches.append((allergens[m.evaluate(assignments[ii]).as_long()], ings[ii]))
matches.sort()
ctx.submit(2, ",".join(m[1] for m in matches))
