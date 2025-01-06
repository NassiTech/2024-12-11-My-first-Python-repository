# Method is in a class bound
class Calculator:
    def add(self, a, b):
        return a + b


my_calculator = Calculator()
print(my_calculator.add(2, 3))
