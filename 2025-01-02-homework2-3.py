# Das Programm sollte:
# 1. Zwei Zahlen als Eingabe akzeptieren.
# 2. Die Summe aller ungeraden Zahlen im Bereich berechnen.
# 3. Die Summe und die Anzahl der ungeraden Zahlen ausgeben.

# enter
x = int(input("x ?"))

y = int(input("y ?"))
# if we consider that one has (independent  from python) to count the last number of the defined range
y = y + 1
i = range(x, y)
# print(i)
sum = 0
z = 0
for n in i:
    if n % 2 != 0:
        sum = sum + int(n)
# we can use n because integer is already defined earlier
        z = z + 1

print(f"the summ is = {sum} \nthe number of odd numbers is {z}")

# number of odd numbers in the range
