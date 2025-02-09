recipes = {}

def add_recipe(name, ingredients):
    recipes[name] = ingredients

def list_recipes():
    for name, ingredients in recipes.items():
        print(f"{name}: {', '.join(ingredients)}")

add_recipe("Pancakes", ["Flour", "Milk", "Eggs"])
list_recipes()
