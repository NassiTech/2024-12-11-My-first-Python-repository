# write a programm where you make a conversion from C->F and vice versa
# 1Farenheit (F)= (Celcius * 9/5) + 32
# Celcius (C) = (Farenheit (F) - 32) * 5/9
# import simple_functions as sf


def F(C):
    return C * 9 / 5 + 32


C = float(input(f"Temperature (C): "))
print(f"Temperature (F): ", F(C))
