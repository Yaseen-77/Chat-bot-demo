import sqlite3
import json
import os

DB_PATH = "database/faq.db"
JSON_PATH = "database/faqs.json"   

def create_db():
    
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Create table
    cur.execute("""
    CREATE TABLE faq (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT,
        category TEXT,
        source TEXT,
        last_updated TEXT
    )
    """)

    # Load JSON data
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Insert into DB
    for item in data:
        question = item.get("QUESTION")
        answer = item.get("ANSWERS")
        category = item.get("CATEGORY", "")
        source = item.get("SOURCE", "")
        last_updated = item.get("LAST UPDATED", "")
        cur.execute(
            "INSERT INTO faq (question, answer, category, source, last_updated) VALUES (?, ?, ?, ?, ?)",
            (question, answer, category, source, last_updated)
        )

    conn.commit()
    conn.close()
    print(f"✅ Database created at {DB_PATH} and {len(data)} FAQs inserted!")

if __name__ == "__main__":
    create_db()
