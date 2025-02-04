# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
# is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

n = int(input("Enter a number? "))
print(
    f"Here is the result for the number  of Fibonacci numbers you want ro generate ", n
)
x = 0
y = 1
for i in range(n):
    z = x + y
    print(z)
    x = y
    y = z
