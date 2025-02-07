import random


def guess_number():
    secret_number = random.randint(0, 99)


counts = 0
high = 99
low = 0
trial = 1

clever_guess = 50

user_input = None
while "C" != user_input:
    user_input = input(f"Is the guess {clever_guess} ?")

    if user_input == "high":
        clever_guess = (50 - low) / 2
        low = low + 1
    if user_input == "low":
        clever_guess = (high / 2 + 50) / 2
        high = high - 1


print(f"You have found the secret number, {clever_guess }")


# guess = int(input("Enter a guessed number between 0 and 99: "))

if __name__ == "__main__":
    results = ["0", "0"]
