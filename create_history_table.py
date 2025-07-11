
import sqlite3

DB_PATH = "/root/smart_bot/db.sqlite3"

create_history_sql = """
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    activity_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(activity_id) REFERENCES activities(id)
);
"""

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(create_history_sql)
    conn.commit()
    conn.close()
    print("✅ Таблица 'history' успешно создана или уже существует.")

if __name__ == "__main__":
    main()
