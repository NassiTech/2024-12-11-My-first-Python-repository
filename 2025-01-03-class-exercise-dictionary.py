dictionary = {
    "Kartofel": "potato",
    "Ameise": "ant",
    "Ei": "egg",
    "Biene": "bee",
    "Affe": "monkey",
    "Wasser": "water",
    "Zimmer": "room",
}
user_input = input("what world would you like to translate ?:").capitalize()
print(f"the translation of {user_input} is {dictionary[user_input]}")
