from lib.models.learner import Learner
from lib.models.course import Course
from lib.models.enrollment import Enrollment
from lib.database import CURSOR, CONN

def main_menu():
    while True:
        print("\n=== 🎓 Learner Management System ===")
        print("1. Add a new learner")
        print("2. View all learners")
        print("3. Add a new course")
        print("4. View all courses")
        print("5. Enroll a learner in a course")
        print("6. View all enrollments")
        print("7. Update learner progress")
        print("8. Find a learner or course by ID")
        print("9. Delete a learner, course, or enrollment")
        print("10. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Learner name: ")
            email = input("Learner email: ")
            try:
                Learner(name, email).save()
                print("✅ Learner added successfully.")
            except Exception as e:
                print(f"❌ {e}")

        elif choice == "2":
            learners = Learner.get_all()
            if learners:
                for learner in learners:
                    print(learner)
            else:
                print("No learners registered yet.")

        elif choice == "3":
            title = input("Course title: ")
            instructor = input("Instructor name: ")
            Course(title, instructor).save()
            print("✅ Course added successfully.")

        elif choice == "4":
            courses = Course.get_all()
            if courses:
                for course in courses:
                    print(course)
            else:
                print("No courses available yet.")

        elif choice == "5":
            learner_id = int(input("Enter learner ID: "))
            course_id = int(input("Enter course ID: "))
            Enrollment(learner_id, course_id).save()
            print("✅ Learner enrolled successfully!")

        elif choice == "6":
            enrollments = Enrollment.get_all()
            if enrollments:
                for e in enrollments:
                    print(f"Enrollment {e[0]} | Learner: {e[1]} | Course: {e[2]} | Progress: {e[3]}%")
            else:
                print("No enrollments yet.")

        elif choice == "7":
            try:
                enrollment_id = int(input("Enter enrollment ID: "))
                progress = int(input("Enter new progress (0–100): "))
                Enrollment.update_progress(enrollment_id, progress)
                print("✅ Progress updated successfully!")
            except ValueError as ve:
                print(f"❌ {ve}")

        elif choice == "8":
            entity = input("Find (learner/course): ").strip().lower()
            if entity == "learner":
                id = int(input("Learner ID: "))
                learner = Learner.find_by_id(id)
                print(learner if learner else "❌ Learner not found.")
            elif entity == "course":
                id = int(input("Course ID: "))
                course = Course.find_by_id(id)
                print(course if course else "❌ Course not found.")
            else:
                print("❌ Invalid option.")

        elif choice == "9":
            entity = input("Delete (learner/course/enrollment): ").strip().lower()
            id = int(input("Enter ID to delete: "))
            if entity == "learner":
                learner = Learner.find_by_id(id)
                if learner:
                    learner.delete()
                    print("✅ Learner deleted.")
                else:
                    print("❌ Learner not found.")
            elif entity == "course":
                course = Course.find_by_id(id)
                if course:
                    course.delete()
                    print("✅ Course deleted.")
                else:
                    print("❌ Course not found.")
            elif entity == "enrollment":
                enrollment = Enrollment.find_by_id(id)
                if enrollment:
                    enrollment.delete()
                    print("✅ Enrollment deleted.")
                else:
                    print("❌ Enrollment not found.")
            else:
                print("❌ Invalid choice.")

        elif choice == "10":
            print("👋 Exiting LMS. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")
