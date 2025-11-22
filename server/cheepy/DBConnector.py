import sqlite3
from server.cheepy.Models import MessageModel


class DBConnector:
    def __init__(self, db_path: str = "cheepy.db"):
        # Allow connection across threads
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

        self._create_tables()
        self._seed_users()

    # ----------------------------
    #  Internal helpers
    # ----------------------------

    def _cursor(self):
        """Create a fresh cursor for each DB operation."""
        return self.conn.cursor()

    def _create_tables(self):
        cur = self._cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Message (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL DEFAULT current_timestamp,
                content TEXT NOT NULL,
                sender INTEGER NOT NULL,
                receiver INTEGER NOT NULL,
                is_image INTEGER NOT NULL,
                FOREIGN KEY (sender) REFERENCES Users(id),
                FOREIGN KEY (receiver) REFERENCES Users(id)
            );
        """)

        self.conn.commit()

    def _seed_users(self):
        """Insert default users if they don't exist."""
        self.insert_user_if_not_exists("max")
        self.insert_user_if_not_exists("mahdokht")

    # ----------------------------
    #  Public methods
    # ----------------------------

    def insert_user_if_not_exists(self, name: str):
        cur = self._cursor()
        cur.execute(
            "INSERT OR IGNORE INTO Users (name) VALUES (?);",
            (name,)
        )
        self.conn.commit()

    def create_message(self, message: MessageModel):
        cur = self._cursor()

        cur.execute("""
            INSERT INTO Message (sender, receiver, content, is_image)
            VALUES (?, ?, ?, ?);
        """, (
            message.sender,
            message.receiver,
            message.content,
            message.is_image
        ))

        self.conn.commit()

    def get_last_message(self):
        cur = self._cursor()

        cur.execute("""
            SELECT id, created_at, content, sender, receiver, is_image
            FROM Message
            ORDER BY datetime(created_at) DESC
            LIMIT 1;
        """)

        row = cur.fetchone()

        if not row:
            return None

        return {
            "id": row["id"],
            "created_at": row["created_at"],
            "content": row["content"],
            "sender": row["sender"],
            "receiver": row["receiver"],
            "is_image": row["is_image"],
        }

    def close(self):
        self.conn.close()
