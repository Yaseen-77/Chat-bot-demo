from flask import Flask, request, jsonify
<<<<<<< HEAD
=======
import sqlite3
>>>>>>> db-dev

app = Flask(__name__)

@app.route("/")
def home():
    return "Server running"

<<<<<<< HEAD
=======
def find_answer(query):
    conn = sqlite3.connect("database/faq.db")
    cur = conn.cursor()
    cur.execute("SELECT answer FROM faq WHERE question LIKE ? LIMIT 1", (f"%{query}%",))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

>>>>>>> db-dev
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "")
<<<<<<< HEAD
    return jsonify({"response": f"You asked: {query}. (DB/AI coming soon)"})
=======

    answer = find_answer(query)
    if answer:
        return jsonify({"response": answer})
    else:
        return jsonify({"response": "Sorry, I couldn’t find this in FAQs. (AI fallback coming soon)"})
>>>>>>> db-dev

if __name__ == "__main__":
    app.run(debug=True)
