# write a programm where you make a conversion from C->F and vice versa
# 1Farenheit (F)= (Celcius * 9/5) + 32
# Celcius (C) = (Farenheit (F) - 32) * 5/9
# import simple_functions as sf


def C(F):
    return 5 / 9 * (F - 32)


F = float(input(f"Temperature (F): "))
print(f"Temperature (C): ", C(F))
