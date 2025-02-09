#users = [
    #{"id": 1, "username": "max", "password": "123456"},
   # {"id": 2, "username": "Anna", "password": "54321"},
#]

#Simulated databank
import hashlib
users []
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdiest()
def login(username, password):

    print(f"my Username: {musername} password {mpassword}")
    user = None
    for u in users:
        if u["username"] == musername and u["password"] == mpassword:
            user = u
    return user


def singup(username, password):
    new_user_id = len(users) + 1
    users.append({"id": new_user_id, "username": musername, "password": mpassword})


username = input("what is your login name: ")
password = input("what is your login password: ")
current_user = login(username, password)
print(f"My logged in user with {username} and {password} is {current_user}")
