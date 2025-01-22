from flask import Flask, json, jsonify, request

# Erstellen einer Flask-Anwendung
app = Flask(__name__)

# load the user list from json file: 
with open('users_data.json', 'r') as file:
    users = json.load(file)

# Definieren einer Route
@app.route("/")
def hello():
    return f"Welcome to '{__file__.rsplit("/")[-1]}'"

# Route 1: /user/<id> 
# Beispiel: http://localhost:6060/user/1 
# Rückgabe: Nutzerdetails wie {"id": 1, "name": "Alice", "email": "alice@example.com"}
@app.route('/user/<id>', methods=['GET'])
def user(id):
    for user in users:
      if user["id"] == int(id):
        #return f"{user}"
        return jsonify(user), 200
      
# Route 2: /login/<id> 
# Beispiel: http://localhost:6060/login/2 
# Rückgabe: "User Bob successfully logged in!" (oder Fehler, falls ID nicht existiert)
@app.route('/login/<id>', methods=['GET'])
def login(id):
    for user in users:
      if user["id"] == int(id):
        return f"User {user["name"]} successfully logged in!"
    return f"No user found with id: {id}"

# Route 3: /search?name=<name> 
# Beispiel: http://localhost:6060/search?name=Charlie 
# Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"
@app.route('/search', methods=['GET'])
def search():
    # Extract query parameters
    name = request.args.get('name')
    for user in users:
      if user["name"] == name:
        return f"Found user: {name}"
    return f"No user found with name: {name}"


# Anwendung starten
if __name__ == "__main__":
    app.run(debug=True)