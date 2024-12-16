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


def calculator(op):

    if op == "+":
        return add(x, y)

    if op == "-":
        return substract(x, y)

    if op == "*":
        return mult(x, y)

    if op == "/":
        return div(x, y)

    if not (op in ["+", "*", "-", "/"]):
        print(f"something went wrong! Focus!")


######################################################################################
# The main part of the programm starts here

x = float(input(f"x :"))
y = float(input(f"y :"))

op = input(f"operation (+ , - , * , /) ? ")
print(calculator(op))
