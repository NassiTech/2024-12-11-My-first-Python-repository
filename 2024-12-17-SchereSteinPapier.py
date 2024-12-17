#### A program that plays “Rock, Paper, Scissors” with the user ###############
# 1. The user should be asked for a selection.
# 2. The program catches incorrect values.
# 3. The computer chooses an option at random.
# 4. The computer's choice and the winner will be displayed on the terminal.
###############################################################################

import random

list = ["Schere", "Stein", "Papier"]

while True:
    user_choice = input("Your choice? ")
    if not (user_choice in list):
        print(f"Input {user_choice} not allowed!")
        exit()

    comp_choice = random.choice(list)

    print(f"Computer choice: {comp_choice}")

    if user_choice == comp_choice:
        print(f"Undecided!")

    else:
        if (
            (user_choice == "Schere" and comp_choice == "Papier")
            or (user_choice == "Stein" and comp_choice == "Schere")
            or (user_choice == "Papier" and comp_choice == "Stein")
        ):
            print(f"You won!")
        else:
            print(f"Computer won!")
        break
