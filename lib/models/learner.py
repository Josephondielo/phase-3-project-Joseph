from lib.database import CURSOR, CONN
import sqlite3

class Learner:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name     
        self.email = email   

    # === Property Methods ===
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Learner name cannot be empty.")
        self._name = value.strip().title()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value or "@" not in value or "." not in value:
            raise ValueError("Invalid email address.")
        self._email = value.strip().lower()

    # === ORM Methods ===
    def save(self):
        # Prevent duplicate emails
        CURSOR.execute("SELECT * FROM learners WHERE email = ?", (self.email,))
        existing = CURSOR.fetchone()
        if existing:
            raise Exception("Learner with this email already exists.")

        CURSOR.execute(
            "INSERT INTO learners (name, email) VALUES (?, ?)",
            (self.name, self.email)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM learners")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], email=row[2]) for row in rows]

    @classmethod
    def find_by_id(cls, learner_id):
        CURSOR.execute("SELECT * FROM learners WHERE id = ?", (learner_id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], name=row[1], email=row[2]) if row else None

    def delete(self):
        if not self.id:
            raise ValueError("Learner must have an ID before deletion.")
        CURSOR.execute("DELETE FROM learners WHERE id = ?", (self.id,))
        CONN.commit()

    def __repr__(self):
        return f"({self.id}) {self.name} - {self.email}"
