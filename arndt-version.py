high = 100
low = 0

clever_guess = 50
user_input = None

print("\nGuess a number from 1-99!\n")

while "C" != user_input:
    user_input = input(f"\nIs the guess {clever_guess}? ")

    if user_input == "high":
        high = clever_guess
        clever_guess = int((clever_guess - low) / 2)

    if user_input == "low":
        low = clever_guess
        clever_guess = int((high + clever_guess) / 2)

print(f"You have found the secret number, {clever_guess }")
