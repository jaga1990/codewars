def cakes(recipe, available):
    result = []
    for ingredient in recipe:
        if ingredient in available:
            result.append(int(available[ingredient]/recipe[ingredient]))
        else:
            return 0
    return min(result)
        
#cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})

cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000})
