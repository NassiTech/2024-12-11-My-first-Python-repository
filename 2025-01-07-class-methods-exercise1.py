# Implement the UML Class-diagram
class Ingredient:
    def __init__(self, name: str, calories_per_100g: int, preparation_time: int):
        self.name = name
        self.calories_per_100g = calories_per_100g
        self.preparation_time = preparation_time


# need to recall the ingredients from class Ingredients


class Recipe:
    def __init__(self, name: str, directions: str):
        self.recipename = name
        self.list_of_ingredients = {}
        self.directions = directions

    # define methods
    def add_ingredient(self, ingr: Ingredient, amount: str):
        self.list_of_ingredients[ingr] = amount
        return

    def Totalcalories(self):
        sum = 0
        for ingr in self.list_of_ingredients:
            sum = sum + ingr.calories_per_100g
        return sum

    def cooking_time(self):
        max = 0
        for ingr in self.list_of_ingredients:
            if ingr.preparation_time > max:
                max = ingr.preparation_time
        return max

    def show_recipe(self):
        return


ingr1 = Ingredient("Apple", 52, 30)
ingr2 = Ingredient("Cherry", 50, 20)
ingr3 = Ingredient("Banana", 90, 20)
ingr4 = Ingredient("Lemonjuice", 22, 5)
ingr5 = Ingredient("Sugar", 390, 0)

Recipe1 = Recipe("fruitcompote", "Dice fruits and add them together")
Recipe1.add_ingredient(ingr1, "300g")
Recipe1.add_ingredient(ingr2, "100g")
Recipe1.add_ingredient(ingr3, "200g")
Recipe1.add_ingredient(ingr4, "2Teesps")
Recipe1.add_ingredient(ingr5, "2Tablesps")

print(Recipe1.Totalcalories(), Recipe1.cooking_time())
exit()
