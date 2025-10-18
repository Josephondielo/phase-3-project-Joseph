from lib.database import CURSOR, CONN

class Course:
    def __init__(self, title, instructor, id=None):
        self.id = id
        self.title = title          
        self.instructor = instructor 

    # === Property Methods ===
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Course title cannot be empty.")
        self._title = value.strip().title()

    @property
    def instructor(self):
        return self._instructor

    @instructor.setter
    def instructor(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Instructor name cannot be empty.")
        self._instructor = value.strip().title()

    # === ORM Methods ===
    def save(self):
        # Prevent duplicate course titles for same instructor
        CURSOR.execute(
            "SELECT * FROM courses WHERE title = ? AND instructor = ?",
            (self.title, self.instructor)
        )
        existing = CURSOR.fetchone()
        if existing:
            raise Exception("This course with the same instructor already exists.")

        CURSOR.execute(
            "INSERT INTO courses (title, instructor) VALUES (?, ?)",
            (self.title, self.instructor)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM courses")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], title=row[1], instructor=row[2]) for row in rows]

    @classmethod
    def find_by_id(cls, course_id):
        CURSOR.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], title=row[1], instructor=row[2]) if row else None

    def delete(self):
        if not self.id:
            raise ValueError("Course must have an ID before deletion.")
        CURSOR.execute("DELETE FROM courses WHERE id = ?", (self.id,))
        CONN.commit()

    def __repr__(self):
        return f"({self.id}) {self.title} - Instructor: {self.instructor}"
