weekdays = ["monday", "tuesday", "wednesday"]
food = []
for x in weekdays:
    for _ in range(2):
        food_input = input(f"what do you want to eat on {x}?")
        food.append(food_input)
print(f"the food plan for the week is:{food}")
