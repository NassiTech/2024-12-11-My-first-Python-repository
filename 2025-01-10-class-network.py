# simulate data base in a private network- It is a dictionary written in jason
user_database = [
    {"id": 1, "email": "max@musenam.de", "password": "12345!"},
    {"id": 2, "email": "ana@musenam.de", "password": "12345"},
]


def login(email, password):
    logged_in_user = None
    for user in user_database:
        if email == user["email"]:
            print("the user exists")
            if password == user["password"]:
                print("the user has the correct password")
                logged_in_user = {
                    "id": user["id"],
                    "email": user["email"],
                }

        else:
            print("the user exists but password is wrong")
            break
        if logged_in_user != None:
            print("the user has successfully logged in")
            return logged_in_user
        else:
            print("the user has not successfully logged in")
            return None


# if we want that the password should not be displayed
email_input = input("Email: ")
password_input = input("Passwort: ")

user = login(email_input, password_input)

print(f"Unser Benutzer: {user}")
