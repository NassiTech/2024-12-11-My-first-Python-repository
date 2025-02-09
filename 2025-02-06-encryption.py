from cryptography.fernet import Fernet

# Generiert einen Verschlüsselungsschlüssel (in einem realen Szenario sollte dieser sicher gespeichert werden)
key = Fernet.generate_key()
cipher = Fernet(key)

# Simulierte Datenbank
users = []


def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()


def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()


def login(musername, mpassword):
    print(f"My Username: {musername} Password: {mpassword}")
    user = None
    for u in users:
        if u["username"] == musername and decrypt_password(u["password"]) == mpassword:
            user = u
    return user  # risk of habing twice the same name in thge data-user list


def signup(musername, mpassword):
    new_user_id = len(users) + 1
    encrypted_password = encrypt_password(mpassword)
    users.append(
        {"id": new_user_id, "username": musername, "password": encrypted_password}
    )


print("Signup:")
username = input("Wie lautet dein login Name: ")
password = input("Wie lautet dein password: ")

signup(
    username, password
)  # here we add the second signup to check the entered username /password
signup(username, password)

print("login")
username = input("Wie lautet dein login Name: ")
password = input("Wie lautet dein password: ")

current_user = login(username, password)

print(f"My Logged in user with {username} and {password} is {current_user}")
