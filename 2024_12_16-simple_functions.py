# 2024-12-16- define mathematical functions to make simple operations
# simulate a calculator function with interactive questions to the user.


def add(x, y):
    return x + y


def mult(x, y):
    return x * y


def substract(x, y):
    return x - y


def div(x, y):
    return x / y


def calculator():
    op = input(f"operation (+ , - , * , /) ? ")
    if op == "+":
        print(add(x, y))

    if op == "-":
        print(substract(x, y))

    if op == "*":
        print(mult(x, y))

    if op == "/":
        print(div(x, y))
    if not (op in ["+", "*", "-", "/"]):
        print(f"something went wrong! Focus!")


#####################################################################
# Here starts the main part of the programm.

x = float(input(f"x :"))
y = float(input(f"y :"))

calculator()
