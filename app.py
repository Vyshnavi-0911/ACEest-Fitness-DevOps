from flask import Flask, jsonify, request

app = Flask(__name__)
members = []
_next_member_id = 1


@app.get("/")
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness & Gym",
        "service": "ACEest Fitness API",
        "endpoints": ["/health", "/members"]
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.get("/members")
def list_members():
    return jsonify(members), 200


@app.post("/members")
def add_member():
    global _next_member_id
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    plan = data.get("plan", "standard")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "A non-empty name is required"}), 400

    member = {"id": _next_member_id, "name": name.strip(), "plan": plan}
    _next_member_id += 1
    members.append(member)
    return jsonify(member), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
