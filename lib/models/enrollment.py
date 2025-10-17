from lib.database import CURSOR, CONN

class Enrollment:
    def __init__(self, learner_id, course_id, progress=0, id=None):
        self.id = id
        self.learner_id = learner_id    # uses property setter
        self.course_id = course_id      # uses property setter
        self.progress = progress        # uses property setter

    # === Property Methods ===
    @property
    def learner_id(self):
        return self._learner_id

    @learner_id.setter
    def learner_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Learner ID must be a positive integer.")
        self._learner_id = value

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Course ID must be a positive integer.")
        self._course_id = value

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        if not isinstance(value, (int, float)) or not 0 <= value <= 100:
            raise ValueError("Progress must be a number between 0 and 100.")
        self._progress = int(value)

    # === ORM Methods ===
    def save(self):
        # Prevent duplicate enrollment (same learner in same course)
        CURSOR.execute(
            "SELECT * FROM enrollments WHERE learner_id = ? AND course_id = ?",
            (self.learner_id, self.course_id)
        )
        existing = CURSOR.fetchone()
        if existing:
            raise Exception("This learner is already enrolled in the selected course.")

        CURSOR.execute(
            "INSERT INTO enrollments (learner_id, course_id, progress) VALUES (?, ?, ?)",
            (self.learner_id, self.course_id, self.progress)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        CURSOR.execute("""
            SELECT e.id, l.name, c.title, e.progress
            FROM enrollments e
            JOIN learners l ON e.learner_id = l.id
            JOIN courses c ON e.course_id = c.id
        """)
        return CURSOR.fetchall()

    @classmethod
    def find_by_id(cls, enrollment_id):
        CURSOR.execute("SELECT * FROM enrollments WHERE id = ?", (enrollment_id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], learner_id=row[1], course_id=row[2], progress=row[3]) if row else None

    def delete(self):
        if not self.id:
            raise ValueError("Enrollment must have an ID before deletion.")
        CURSOR.execute("DELETE FROM enrollments WHERE id = ?", (self.id,))
        CONN.commit()

    @classmethod
    def update_progress(cls, enrollment_id, progress):
        if not 0 <= progress <= 100:
            raise ValueError("Progress must be between 0 and 100.")
        CURSOR.execute("UPDATE enrollments SET progress = ? WHERE id = ?", (progress, enrollment_id))
        CONN.commit()

    def __repr__(self):
        return f"Enrollment({self.id}) Learner:{self.learner_id} Course:{self.course_id} Progress:{self.progress}%"
