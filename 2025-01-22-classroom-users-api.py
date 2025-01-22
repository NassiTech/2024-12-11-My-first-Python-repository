from flask import Flask, request, json
from data.users_list import users

app = Flask(__name__)


@app.route("/user/<user_id>", methods=["GET"])
def get_user_id(user_id):
    final_user = None

    for user in users:
        if user["id"] == user_id:
            return final_user
    if final_user == None:
        return "User not found"
    return f"the final_user is {final_user}"


@app.route("/users/login/", methods=["POST"])
def glogin():
    credentials = request.get_json()
    username = credentials["usewrname"]
    password = credentials["password"]
    return f"Hello {username} {password}"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
