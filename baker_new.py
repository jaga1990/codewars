def cakes(recipe, available):
    print(min(available.get(k, 0)/recipe[k] for k in recipe))

cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000})