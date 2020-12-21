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

    G = nx.Graph()
    for k, v in can_contain.items():
        G.add_node(k, bipartite=0)
        for vv in v:
            G.add_node(vv, bipartite=1)
            G.add_edge(k, vv)
    
    mapping = [(v, k) for k, v in nx.bipartite.matching.hopcroft_karp_matching(G, all_allergens).items() if k in all_allergens]
    mapping = ",".join(x[0] for x in sorted(mapping, key=lambda x: x[1]))
    print(mapping)

    ctx.submit(2, None)
