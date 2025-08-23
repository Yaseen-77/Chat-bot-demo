from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "Server running"

def find_answer(query):
    conn = sqlite3.connect("database/faq.db")
    cur = conn.cursor()
    cur.execute("SELECT answer FROM faq WHERE question LIKE ? LIMIT 1", (f"%{query}%",))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "")

    answer = find_answer(query)
    if answer:
        return jsonify({"response": answer})
    else:
        return jsonify({"response": "Sorry, I couldn’t find this in FAQs. (AI fallback coming soon)"})

if __name__ == "__main__":
    app.run(debug=True)
