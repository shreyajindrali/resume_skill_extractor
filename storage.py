import json
import os

DB_FILE = "resume_db.json"

def save_data(data):
    all_data = load_all_data()
    all_data.append(data)
    with open(DB_FILE, "w") as f:
        json.dump(all_data, f, indent=4)

def load_all_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)
