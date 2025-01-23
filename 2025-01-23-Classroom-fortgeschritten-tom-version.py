from flask import Flask, request
from data.users_list import users

app = Flask(__name__)


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    final_user = None

    for u in users:
        if u["id"] == user_id:
            final_user = u

    if final_user == None:
        return "User could not be found "

    return f"The User is {final_user}"


# Route 3: /search?name=<name>
# Beispiel: http://localhost:6060/search?name=Charlie
# Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"
@app.route("/search", methods=["GET"])
def get_user_by_name():
    final_user = None
    name = request.args.get("name")
    for u in users:
        if u["firstName"] == name:
            final_user = u

    if final_user == None:
        return "User could not be found "

    return f"The User is {final_user}"


# @app.route(
#     "/users/login", methods=["POST"]
# )  # localhost:<PORT>/users/login, body: {"username": <USER_NAME>, "password": <PASSWORD>}
# def login():
#     credentials = request.get_json()
#     username = credentials["username"]
#     password = credentials["password"]

#     final_user = None
#     for u in users:
#         if u["username"] == username:
#             final_user = u

#     if final_user == None:
#         return "User could not be found "

#     if final_user["password"] != password:
#         return f"User with username {username} exists but the password {password} is incorrect"
#     # Now you can access the user based on email and password and return if valid credentials
#     return f"Hallo {credentials} {username} {password}"
# @app.route("/users/signup", methods=["POST"])  # localhost:<PORT>/users/signup,


# def signup():
#     new_user = request.get_json()
#     if (
#         "username" not in new_user
#         or "firstName" not in new_user
#         or "password" not in new_user
#         or "familyName" not in new_user
#     ):
#         return "Parameters are missing", 400

#     nextId = max([p["id"] for p in users], default=0) + 1
#     new_user["id"] = nextId

#     return new_user, 201


# 1. Postman installieren
# 2. url eingeben, POST Befehl aushwählen --> siehe Screenshot
# 3. Ausführen und veschiedene Parameter im  body angeben
# 4. Versuchen den richtigen Benutzer zu bekommen
# 5. Versucht eine weitere post anfrage mit signup zu erstellen,
# welche Route einen neuen Nutzer in die Liste einfügt
# 6. Zusatz: Wendet sinvolle Fälle für PUT und DELETE an (z.B udpate username, delete user)
# 7. Schwierig: Schreibt die Nutzer-liste in eine Datei, sodass die Liste aktuell bleibt, auch nach Beenden des Program
@app.route(
    "/users/login", methods=["POST"]
)  # localhost:<PORT>/users/login, body: {"username": <USER_NAME>, "password": <PASSWORD>}
def login():
    credentials = request.get_json()
    username = credentials["username"]
    password = credentials["password"]

    final_user = None
    for u in users:
        if u["username"] == username:
            final_user = u

    if final_user == None:
        return "User could not be found "
    # Now you can access the user based on email and password and return if valid credentials
    return f"Hallo {credentials} {username} {password}"


@app.route("/users/signup", methods=["POST"])
def signup():
    new_user = request.json()
    if (
        "username" not in new_user
        or "password" not in new_user
        or "name" not in new_user
        or "familyName" not in new_user
    ):
        return " One of the parameters is missing or wrong", 400
    nextid = max([p["id"] for p in users], default=0) + 1
    users.append(new_user)
    new_user["id"] = nextid
    return new_user, 201
    if password != password:
        

if __name__ == "__main__":
    app.run(debug=True, port=6060)
