from puzzle import PuzzleContext
from collections import defaultdict
import networkx as nx



with PuzzleContext(year=2020, day=21) as ctx:
    foods = []
    for line in ctx.nonempty_lines:
        ingredients, allergens = line.split(" (")
        allergens = allergens[:-1].replace("contains ", "").split(", ")
        ingredients = ingredients.split(" ")
        foods.append((allergens, ingredients))


    all_allergens = set()
    all_ings = set()
    can_contain = dict()
    counts = defaultdict(int)
    for allergens, ingredients in foods:
        for ing in ingredients:
            counts[ing] += 1
            all_ings.add(ing)
        for allergen in allergens:
            all_allergens.add(allergen)
            if allergen not in can_contain:
                can_contain[allergen] = set(ingredients)
            else:
                can_contain[allergen] &= set(ingredients)

    unused = all_ings.copy()    
    for k, v in can_contain.items():
        for ing in v:
            if ing in unused:
                unused.remove(ing)

    ans1 = 0
    for x in unused:
        ans1 += counts[x]
    ctx.submit(1, ans1)

    mapping = []
    while len(can_contain) > 0:
        picked = None
        for k in can_contain:
            if len(can_contain[k]) == 1:
                picked = k
                break
        assert picked is not None
        ing = list(can_contain[picked])[0]
        for k, v in can_contain.items():
            if ing in v:
                v.remove(ing)
        mapping.append((ing, picked))
        del can_contain[picked]
    
    ans2 = ",".join(x[0] for x in sorted(mapping, key=lambda x: x[1]))

    ctx.submit(2, ans2)
