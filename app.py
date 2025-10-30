from flask import Flask, request, abort, render_template, redirect, url_for

app = Flask(__name__)

# In-memory “database” of users
users = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
     {"id": 3, "name": "Hamza", "age": 981}
]

# Home page
@app.route("/")

    return render_template("index.html")

# View users
@app.route("/users")
def get_users():
    return render_template("users.html", users=users)

# Add a new user (POST via form)
@app.route("/users", methods=["POST"])
def create_user():
    name = request.form.get("name")
    age = request.form.get("age")
    if not name or not age:
        abort(400, "Name and age required")
    
    try:
        age = int(age)
    except ValueError:
        abort(400, "Age must be a number")
    
    new_user = {"id": len(users)+1, "name": name, "age": age}
    users.append(new_user)
    return redirect(url_for("get_users"))

if __name__ == "__main__":
    app.run(debug=True)
