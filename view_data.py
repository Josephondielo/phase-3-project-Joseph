from lib.database import CURSOR, CONN

def view_all_data():
    print("\n=== 📘 LEARNERS ===")
    learners = CURSOR.execute("SELECT * FROM learners").fetchall()
    if learners:
        for l in learners:
            print(f"ID: {l[0]} | Name: {l[1]} | Email: {l[2]}")
    else:
        print("No learners found.")

    print("\n=== 📗 COURSES ===")
    courses = CURSOR.execute("SELECT * FROM courses").fetchall()
    if courses:
        for c in courses:
            print(f"ID: {c[0]} | Title: {c[1]} | Instructor: {c[2]}")
    else:
        print("No courses found.")

    print("\n=== 📙 ENROLLMENTS ===")
    enrollments = CURSOR.execute("""
        SELECT e.id, l.name, c.title, e.progress
        FROM enrollments e
        JOIN learners l ON e.learner_id = l.id
        JOIN courses c ON e.course_id = c.id
    """).fetchall()

    if enrollments:
        for e in enrollments:
            print(f"ID: {e[0]} | Learner: {e[1]} | Course: {e[2]} | Progress: {e[3]}%")
    else:
        print("No enrollments found.")

    CONN.close()

if __name__ == "__main__":
    view_all_data()
