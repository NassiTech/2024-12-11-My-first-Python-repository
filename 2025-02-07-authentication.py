import hashlib

from cryptography.fernet import Fernet

users_list = []

# Generiert einen Verschlüsselungsschlüssel (in einem realen Szenario sollte dieser sicher gespeichert werden)
key = Fernet.generate_key()
cipher = Fernet(key)


def encrypt_value(value):
    return cipher.encrypt(value.encode()).decode()


def decrypt_value(value):
    return cipher.decrypt(value.encode()).decode()


def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()


def login(musername, mpassword):
    print(f"My Username: {musername} Password: {mpassword}")
    user = None
    hashed_password = hash_password(mpassword)
    for u in users_list:
        if u["username"] == musername and u["password"] == hashed_password:
            user = u
            break

    return user


def signup(musername, mpassword, credit_card):
    for u in users_list:
        if u["username"] == musername:
            print("User exists already, please Login")
            return

    new_user_id = len(users_list) + 1  # 1, 2,
    hashed_password = hash_password(mpassword)
    encrypted_credit_card = encrypt_value(credit_card)
    users_list.append(
        {
            "id": new_user_id,
            "username": musername,
            "password": hashed_password,
            "credit_card": encrypted_credit_card,
        }
    )


def buy_product(musername):
    user = None
    for u in users_list:
        if u["username"] == musername:
            user = u
            break
    credit_card_encryted = user["credit_card"]
    credit_card = decrypt_value(credit_card_encryted)
    print(f"User has bought the item with credit card {credit_card}")


username = input("Wie lautet dein login Name: ")
password = input("Wie lautet dein password: ")
credit_card = input("Wie lautet Kreditkarte: ")

print("sign up")
signup(username, password, credit_card)

print(users_list)
print("Login")
current_user = login(
    username,
    password,
)

buy_product(username)

print(f"My Logged in user with {username} and {password} is {current_user}")


##Tom Schiffmann
# 11:07
# python3 -m pip3 list

# - WSL
# - pip3 install cryptography
# - Python ausführen
