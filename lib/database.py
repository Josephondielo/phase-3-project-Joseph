# lib/database.py
import sqlite3

# Connect to or create database
CONN = sqlite3.connect('db/database.db')
CURSOR = CONN.cursor()

def create_tables():
    """Create database tables for learners, courses, and enrollments."""
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS learners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE
        )
    ''')

    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            instructor TEXT NOT NULL
        )
    ''')

    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            learner_id INTEGER,
            course_id INTEGER,
            progress INTEGER DEFAULT 0,
            FOREIGN KEY (learner_id) REFERENCES learners(id),
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    ''')

    CONN.commit()
