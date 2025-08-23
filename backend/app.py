from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server running"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "")
    return jsonify({"response": f"You asked: {query}. (DB/AI coming soon)"})

if __name__ == "__main__":
    app.run(debug=True)
