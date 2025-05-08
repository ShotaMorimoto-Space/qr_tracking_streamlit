# backend/init_db.py
import sqlite3
import os

os.makedirs("tracking_app_db", exist_ok=True)

conn = sqlite3.connect("tracking_app_db/access_logs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS access_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    zebra_id TEXT NOT NULL,
    campaign_name TEXT NOT NULL,
    uid TEXT UNIQUE NOT NULL,
    target_url TEXT NOT NULL,
    access_count INTEGER DEFAULT 0,
    last_accessed_at DATETIME
);
""")

conn.commit()
conn.close()

print("✅ access_logsテーブルを作成しました！")