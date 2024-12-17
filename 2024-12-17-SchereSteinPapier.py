#### A program that plays “Rock, Paper, Scissors” with the user ###############
# 1. The user should be asked for a selection.
# 2. The program catches incorrect values.
# 3. The computer chooses an option at random.
# 4. The computer's choice and the winner will be displayed on the terminal.
###############################################################################

import random

list = ["Schere", "Stein", "Papier"]


user_choise = input("Your choice? ")
if not (user_choise in list):
    print(f"Input {user_choise} not allowed!")
    exit()

comp_choise = random.choice(list)

print(f"Computer choice: {comp_choise}")

if user_choise == comp_choise:
    print(f"Undecided!")
else:
    if (
        (user_choise == "Schere" and comp_choise == "Papier")
        or (user_choise == "Stein" and comp_choise == "Schere")
        or (user_choise == "Papier" and comp_choise == "Stein")
    ):
        print(f"You win!")
    else:
        print(f"Computer wins!")
