import hashlib

# Simulierte Datenbank
users = []


def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()


def login(musername, mpassword):
    print(f"My Username: {musername} Password: {mpassword}")
    user = None
    hashed_password = hash_password(mpassword)
    for u in users:
        if u["username"] == musername and u["password"] == hashed_password:
            user = u
    return user


def signup(musername, mpassword):
    new_user_id = len(users) + 1
    hashed_password = hash_password(mpassword)
    users.append(
        {"id": new_user_id, "username": musername, "password": hashed_password}
    )


print("Signup:")
username = input("Wie lautet dein login Name: ")
password = input("Wie lautet dein password: ")

signup(username, password)

print("Login:")
username = input("Wie lautet dein login Name: ")
password = input("Wie lautet dein password: ")

current_user = login(username, password)

print(f"My Logged in user with {username} and {password} is {current_user}")
