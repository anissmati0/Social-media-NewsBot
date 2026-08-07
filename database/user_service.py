import sqlite3
from settings import DEFAULT_SETTINGS
from models import User

base_path = "database/database.db"

def init_database():
    connect = sqlite3.connect(base_path)
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                    user_id INTEGER PRIMARY KEY,
                    text_color TEXT,
                    gradient TEXT,
                    platform TEXT,
                    tone TEXT,
                    language TEXT
                    )""")

    connect.commit()
    connect.close()

def create_user(telegram_id):
    connect = sqlite3.connect(base_path)
    cursor = connect.cursor()

    user = User(telegram_id=telegram_id,
                text_color=DEFAULT_SETTINGS["text_color"],
                gradient_color=DEFAULT_SETTINGS["gradient_color"],
                platform=DEFAULT_SETTINGS["platform"],
                tone=DEFAULT_SETTINGS["tone"],
                language=DEFAULT_SETTINGS["language"])

    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?)", 
                   (user.telegram_id,
                    user.text_color,
                    user.gradient_color,
                    user.platform,
                    user.tone,
                    user.language))

    connect.commit()
    connect.close()

def user_exists(telegram_id: str) -> bool:
    connect = sqlite3.connect(base_path)
    cursor = connect.cursor()

    cursor.execute("SELECT 1 FROM users WHERE user_id = ? LIMIT 1", (telegram_id,))
    exists = cursor.fetchall()
    connect.close

    return bool(exists)

if __name__ == "__main__":
    init_database()
    #create_user(123)
    #create_user(1234)
    print(user_exists(telegram_id=1235))