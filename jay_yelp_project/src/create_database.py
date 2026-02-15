import sqlite3
import json
from pathlib import Path

# Set correct base directory
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DB_PATH = DATA_DIR / "yelp_IN_PA.db"
JSON_PATH = DATA_DIR / "yelp_in_pa_business.json"

print("Creating database...")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS businesses (
    business_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    state TEXT,
    stars REAL,
    review_count INTEGER
)
""")

count = 0

# Insert records
with open(JSON_PATH, "r", encoding="utf-8") as file:
    for line in file:
        b = json.loads(line)
        cursor.execute("""
            INSERT OR IGNORE INTO businesses
            (business_id, name, city, state, stars, review_count)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            b["business_id"],
            b["name"],
            b["city"],
            b["state"],
            b["stars"],
            b["review_count"]
        ))
        count += 1

conn.commit()
conn.close()

print(f"Database ready. {count} records inserted.")

