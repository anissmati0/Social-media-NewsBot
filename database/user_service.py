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

    connect.commit()
    connect.close()

    return bool(exists)

def get_user_settings(telegram_id):
    connect = sqlite3.connect(base_path)
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM USERS WHERE user_id = ? LIMIT 1", (telegram_id, ))
    data = cursor.fetchall()

    settings = {
                "text_color": data[0][1],
                "gradient_color": data[0][2],
                "platform": data[0][3],
                "tone": data[0][4],
                "language": data[0][5],
            }

    connect.commit()
    connect.close()
    
    return settings

class update_settings:
    def text_color(telegram_id, new_color: str):
        connect = sqlite3.connect(base_path)
        cursor = connect.cursor()

        cursor.execute("UPDATE users SET text_color = ? WHERE user_id = ?", (new_color, telegram_id,))
        connect.commit()
        connect.close()

    def gradient_color(telegram_id, new_gradient: str):
            connect = sqlite3.connect(base_path)
            cursor = connect.cursor()
    
            cursor.execute("UPDATE users SET gradient = ? WHERE user_id = ?", (new_gradient, telegram_id,))
            connect.commit()
            connect.close()

    def platform(telegram_id, new_platform: str):
                connect = sqlite3.connect(base_path)
                cursor = connect.cursor()
        
                cursor.execute("UPDATE users SET platform = ? WHERE user_id = ?", (new_platform, telegram_id,))
                connect.commit()
                connect.close()

    def tone(telegram_id, new_tone: str):
                    connect = sqlite3.connect(base_path)
                    cursor = connect.cursor()
            
                    cursor.execute("UPDATE users SET tone = ? WHERE user_id = ?", (new_tone, telegram_id,))
                    connect.commit()
                    connect.close()

    def language(telegram_id, new_language: str):
                        connect = sqlite3.connect(base_path)
                        cursor = connect.cursor()
                
                        cursor.execute("UPDATE users SET language = ? WHERE user_id = ?", (new_language, telegram_id,))
                        connect.commit()
                        connect.close()

def reset_settings(telegram_id):
        connect = sqlite3.connect(base_path)
        cursor = connect.cursor()

        data = (DEFAULT_SETTINGS['text_color'],
                DEFAULT_SETTINGS['gradient_color'],
                DEFAULT_SETTINGS['platform'],
                DEFAULT_SETTINGS['tone'],
                DEFAULT_SETTINGS['language'],
                telegram_id)

        query = """
                UPDATE users 
                SET text_color = ?, 
                gradient = ?, 
                platform = ?,
                tone = ?,
                language = ?
                WHERE user_id = ?
            """

        cursor.execute(query, data)

        connect.commit()
        connect.close()


if __name__ == "__main__":
    init_database()
    #create_user(123)
    #create_user(1234)
    #print(user_exists(telegram_id=123))
    #update_settings.text_color(123, "#0986")
    #update_settings.gradient_color(123, "#0986")
    #update_settings.platform(123, "facebook")
    #update_settings.tone(123, "proffessional")
    #update_settings.language(123, "ar")
    reset_settings(123)
    print(get_user_settings(123))