from flask import Flask, request

app = Flask(__name__)


users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]


@app.route("/user/<user_id", methods=["GET"])
def get_user_by_id(id):
    final_user = None

    for user in users:
        if user["id"] == user_id:
            return final_user
        if final_user == None:
            return "User not found"
        return f"the final_user is {final_user}"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
