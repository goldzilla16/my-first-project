from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory “database” of users
users = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30}
]

# Home route
@app.route("/")
def home():
    return jsonify({"message": "Hello, CI/CD World!"})

# Add two numbers
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

# Multiply two numbers
@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    return jsonify({"result": a * b})

# List all users
@app.route("/users")
def get_users():
    return jsonify(users)

# Add a new user (POST)
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        abort(400, description="Missing name or age")
    
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "age": data["age"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True)
