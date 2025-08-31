from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from models import users, notes

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # change in production
jwt = JWTManager(app)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Flask JWT API"}), 200

# ---------- AUTH ----------
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {"password": password}
    return jsonify({"message": f"User {username} registered"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username not in users or users[username]["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(identity=username)
    return jsonify(access_token=token), 200

# ---------- PROTECTED ROUTES ----------
@app.route("/notes", methods=["GET"])
@jwt_required()
def get_notes():
    return jsonify(notes), 200

@app.route("/notes", methods=["POST"])
@jwt_required()
def add_note():
    data = request.get_json()
    note_id = len(notes) + 1
    notes[note_id] = data.get("note")
    return jsonify({"message": "Note added", "id": note_id}), 201

@app.route("/notes/<int:note_id>", methods=["DELETE"])
@jwt_required()
def delete_note(note_id):
    if note_id not in notes:
        return jsonify({"error": "Note not found"}), 404
    del notes[note_id]
    return jsonify({"message": f"Note {note_id} deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
