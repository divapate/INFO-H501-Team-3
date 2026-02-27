import sqlite3
import matplotlib.pyplot as plt
from pathlib import Path

# Correct base directory
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DB_PATH = DATA_DIR / "yelp_IN_PA.db"
OUTPUT_PATH = DATA_DIR / "state_distribution.png"

print("Generating visualization...")

# Connect to database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
SELECT state, COUNT(*) 
FROM businesses 
GROUP BY state
""")

data = cursor.fetchall()

states = [row[0] for row in data]
counts = [row[1] for row in data]

# Create bar chart
plt.figure()
plt.bar(states, counts)
plt.xlabel("State")
plt.ylabel("Number of Businesses")
plt.title("Business Distribution in IN and PA")

plt.savefig(OUTPUT_PATH)
plt.close()

conn.close()

print("Visualization created successfully.")

