# calculate the factorial from with the formula
# n! = n*(n-1)!
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# here the program starts ....

n = int(input("N? "))
print(f"n! = ", factorial(n))
