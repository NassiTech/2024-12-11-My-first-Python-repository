# Exercise 3
# Create a pattern with a nested loop. Example:
# The user enters the number of lines and the program outputs the following pattern:


n = int(input("repetition ? "))  # we decide for the repetition like proposed 5
for i in range(n + 1):  # to get 5 times the pattern
    for k in range(i):  # the inner loop once we fixed the outer loop
        print("*", end="")  # to supress the end of line
    print("\n")  # junp to the new line to print the next pattern
