import sqlite3
from telegram import Message

def init_db():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            date TEXT,
            text TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_message(message: Message):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (username, date, text)
        VALUES (?, ?, ?)
    ''', (message.from_user.username, message.date, message.text))
    conn.commit()
    conn.close()

def retrieve_messages_in_batches(batch_size: int):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM messages')
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        for row in batch:
            yield {
                'username': row[1],
                'date': row[2],
                'text': row[3]
            }
    conn.close()
