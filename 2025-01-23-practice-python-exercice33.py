# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

# Welcome to birthday dictionary
# version 2 : eimport data list
# from data.birthday_dictionary import name
# version 1 list/ dictionary in the body
# birthday_dictionary = [
# {"name": "Albert Einstein", "birthday": "March_14_1879"},
# {"name": "Benjamin Franklin", "birthday": "January_17_1706"},
# {"name": "Ada Lovelace", "birthday": "October_10_1815"}
# ]
# version2 dictionary in a data file
# from data.birthday_dictionary import birthday_dictionary
# exercise 34 with json

from flask import json

# load the user list from json file:
file = open("birthday_dictionary.json", "r")
birthday_dictionary = json.load(file)
file.close()

for p in birthday_dictionary:
    print(f"{p['name']}")

print("Who's birthday do you want to look up? ")

user_input = input("Enter a name? ")

result = None

for p in birthday_dictionary:
    if user_input == p["name"]:
        print(f"{user_input} s birthday is {p['birthday']}")
        result = p["birthday"]

if result == None:
    print(f"Sorry inexistant in our dictionary! ")
else:
    print(f"Enter new name")
new_name = input("Enter a new name? ")
new_bday = input("Enter the birthdate? ")
new_entry = {}
new_entry["name"] = new_name
new_entry["birthday"] = new_bday
birthday_dictionary.append(new_entry)
# serialize with json.dump.->
# it will write the serialized data in the json file
file = open("birthday_dictionary.json", "w")
# file.write(json.dump(birthday_dictionary))
json.dump(birthday_dictionary, file)
file.close()

print()

# if __name__ == "__main__":
# nextId = max([p["id"] for p in users], default=0) + 1
#     new_user["id"] = nextId
