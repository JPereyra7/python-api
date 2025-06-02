from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulerad "databas" i minnet
users = []
cars = []

# POST – skapa ny user
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    users.append(data)
    return jsonify(data), 201

@app.route("/create-cars", methods=["POST"])
def create_cars():
    data = request.get_json()
    cars.append(data)
    return jsonify(data), 201

# GET – hämta alla users
@app.route("/get-users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/get-cars", methods=["GET"])
def get_cars():
    return jsonify(cars), 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)