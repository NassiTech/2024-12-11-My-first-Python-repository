# first exercise
firstname = input("firstname ?")
lastname = input("lastname? ")
print(firstname + " " + lastname)

print(f"firstname: {firstname} lastname: {lastname}")

# second exercise : add numbers
first_number = int(input("first number ?"))
second_number = int(input("second number? "))
print(f"the summ is:  {first_number + second_number}")

# If condition
first_number = int(input("number ? "))
if first_number >= 0:
    print("positive number or zero")
else:
    print("negative number")
