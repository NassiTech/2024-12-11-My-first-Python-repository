# Exercise 1 : count how many times somethings occurs

# enter the text
user_input = "Là où nous vivions jadis, il n y avait ni autos, ni taxis, ni autobus"
# select the letter to be counted
character = "i"
# we use method count
count = user_input.count(character)
count = 0
for l in user_input:
    if l == character:
        count = count + 1
print(f"the character '{character}' appears {count} times. ")
# there is no "e" in the text ;))
# change to "i"!!
