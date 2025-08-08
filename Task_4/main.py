import json
from flask import Flask, request, jsonify

app = Flask(__name__)
DATA_FILE = "users.json"
def load_users():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users():
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

users = load_users()
next_id = max(map(int, users.keys()), default=0) + 1 if users else 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if str(user_id) in users:
        return jsonify(users[str(user_id)]), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email required"}), 400
    
    users[str(next_id)] = {
        "name": data["name"],
        "email": data["email"],
        "phone": data.get("phone", ""),
        "place": data.get("place", "")
    }
    save_users()
    next_id += 1
    return jsonify({"message": "User created"}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if str(user_id) not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    users[str(user_id)].update(data)
    save_users()
    return jsonify({"message": "User updated"}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if str(user_id) not in users:
        return jsonify({"error": "User not found"}), 404
    
    del users[str(user_id)]
    save_users()
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
