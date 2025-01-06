# Exercise 2
# write a programm that
# asks the user to enter 5 numbers.
# Ue a loop to calculate the summ and the mean value.
# prints the result


numbers = []
for _ in range(5):
    numbers.append(float(input("enter number ? ")))

print(numbers)
sum = 0
for number in numbers:
    sum = sum + number

print(sum)
mean_value = sum / 5
print(mean_value)
