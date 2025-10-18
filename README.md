# Learner Management System (Phase 3 Project)

## Description

The Learner Management System (LMS) is a Command Line Interface (CLI) and Object-Relational Mapping (ORM) application built in Python.
It helps instructors and administrators manage learners, courses, and enrollments efficiently — all from the terminal.

This project simulates a real-world school or training center environment where multiple learners take different courses and track their learning progress.
It allows users to perform actions such as adding learners, viewing available courses, enrolling learners into courses, and updating progress.

## Features

- Add new learners with a name and email address.

- View a complete list of registered learners.

- Prevent duplicate learner entries by enforcing unique email constraints.

- Add and view all available courses in the system.

- Each course stores a title and an instructor’s name.

- Easily extendable to include new courses or delete existing ones.

- Enroll any learner into one or multiple courses.

- View all learner-course enrollments in a clear format.

- Update and track learner progress (in percentages).

- Find learners, courses, or enrollments by ID.

- Delete learners, courses, or enrollments directly from the CLI.

## Overview

The application runs in your terminal and provides an interactive menu for managing a training system.

You can:

- Register learners and instructors,

- Add courses,

- Enroll learners,

- Track learner progress,

- And manage all data stored persistently in an SQLite database.

The system uses Object-Oriented Programming principles and a custom-built ORM layer for database interactions — no external frameworks are required.

## Technologies Used
Technology	Purpose
Python 3.x	Core language
SQLite3	Local database
CLI (Command-Line Interface)	User interaction
OOP & ORM	Data management and modeling
Git & GitHub	Version control and repository hosting

## Project Structure

phase-3-project-joseph/
```│
├── db/
│ └── database.db        # SQLite database file storing all data
│
├── lib/
│ ├── pycache/           # Auto-generated Python cache files
│ │
│ ├── cli.py             # Main CLI menu logic for user interaction
│ ├── database.py        # Database connection, setup, and cursor/connection objects
│ │
│ ├── models/            # Folder containing ORM-style models
│ │ ├── init.py          # Marks models folder as a package
│ │ ├── learner.py       # Learner model — manages learner info (name, email)
│ │ ├── course.py        # Course model — manages course details (title, instructor)
│ │ └── enrollment.py    # Enrollment model — links learners to courses and tracks progress
│
├── venv/                # Virtual environment (contains dependencies, not pushed to Git)
│
├── main.py              # Entry point for running the CLI application
├── view_data.py         # Script to view all database records at once (learners, courses, enrollments)
├── requirements.txt     # Lists all project dependencies
├── README.md            # Project documentation (this file)
└── .gitignore           # Specifies files and folders Git should ignore
```

## Installation
1️⃣ Clone the Repository:

    git clone https://github.com/Josephondielo/phase-3-project-joseph.git

    cd phase-3-project-joseph

2️⃣ Create and Activate a Virtual Environment

Windows:
    
    python -m venv venv

    venv\Scripts\activate

macOS / Linux:

    python3 -m venv venv

    source venv/bin/activate

3️⃣ Install Dependencies

    pip install -r requirements.txt

## How to Run the Project

Run the CLI app:

    python main.py


Follow the on-screen instructions:

=== 🎓 Learner Management System ===
1. Add a new learner
2. View all learners
3. Add a new course
4. View all courses
5. Enroll a learner in a course
6. View all enrollments
7. Update learner progress
8. Find a learner or course by ID
9. Delete a learner, course, or enrollment
10. Exit

    ### View All Data 

    Run from main CLI

        python view_data.py

    Sample output:
    ```
        === 📘 LEARNERS ===
        ID: 1 | Name: John Okumu | Email: john12@gmail.com
        ID: 3 | Name: Evans Kelly | Email: evan2-@gmail.com
        ID: 4 | Name: Beatrice Akoth | Email: bt112-@gmail.com

        === 📗 COURSES ===
        ID: 1 | Title: Mechanics | Instructor: Dr. TOm
        ID: 2 | Title: Botany | Instructor: Prof Indandasi
        ID: 3 | Title: Zoology | Instructor: Miss Jennifer
        ID: 4 | Title: Mathematics | Instructor: Dr. Njoroge
        ID: 5 | Title: Cosmology | Instructor: Dr. Sing

        === 📙 ENROLLMENTS ===
        ID: 3 | Learner: Beatrice Akoth | Course: Mathematics | Progress: 72%
        


## Database Relationships

One-to-Many Relationship:

Learner (1) ───< Enrollment >───(1) Course

```
Table	                    Description
learners	            Stores learner info (id, name, email)
courses	                Stores course info (id, title, instructor)
enrollments	            Connects learners and courses with progress tracking
```

## ORM Methods Implemented
```
Method	                                   Description

save()	                                  Inserts a new record into the database
get_all()	                              Retrieves all records
find_by_id(id)	                          Finds a record by ID
delete()	                              Removes a record
update_progress() (Enrollment)	          Updates learner progress
Property validation	                      Ensures correct field data
```

## Input Validation & Error Handling

- Ensures learner email uniqueness

- Validates progress between 0–100%

- Prevents empty fields for learners and courses

- Provides helpful error messages for invalid input

## Example CLI Workflow
```
1️⃣ Add Learners

Select an option: 1
Learner name: Joseph
Learner email: joseph@gmail.com
✅ Learner added successfully.


2️⃣ Add Courses

Select an option: 3
Course title: Mechanics
Instructor name: Dr. Obwaku
✅ Course added successfully.


3️⃣ Enroll Learner

Select an option: 5
Enter learner ID: 1
Enter course ID: 1
✅ Learner enrolled successfully!


4️⃣ View Enrollments

Select an option: 6
Enrollment 1 | Learner: Joseph | Course: Python Basics | Progress: 0%


5️⃣ Update Progress

Select an option: 7
Enter enrollment ID: 1
Enter new progress (0–100): 80
✅ Progress updated successfully!
```

## Author

Joseph Ondielo
Email: josebonagain@gmail.com

## License

MIT License