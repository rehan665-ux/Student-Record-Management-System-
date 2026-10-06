# 🎓 Student Record Management System

A **Python beginner-to-intermediate project** that allows users to manage student records using **JSON file storage, functions, lists, dictionaries, loops, conditions, exception handling, and user input**.

## 📌 Project Overview

The **Student Record Management System** is a menu-based Python program for managing student information.

The program allows users to:

* ➕ Add students
* 📋 View all students
* 🔎 Search for a student
* ✏️ Update student information
* 🗑️ Delete student records
* 🚪 Exit the program

Student records are stored permanently in a **`students.json`** file, so the data can be used again when the program is restarted.

Each student record contains:

* 🆔 Student ID
* 👤 Student Name
* 🎂 Age
* 📚 Course/Class

## 🚀 Features

* ➕ Add a new student

* 📋 View all student records

* 🔎 Search students using Student ID

* ✏️ Update existing student information

* 🗑️ Delete student records

* 💾 Save records permanently in a JSON file

* 📂 Load existing records when the program starts

* ⚠️ Validate user input

* 🚫 Prevent duplicate Student IDs

* 🔐 Ask for confirmation before deleting a student

* 🛑 Handle invalid file and number input

* 🖥️ Simple menu-based interface

## 🛠️ Python Concepts Used

This project demonstrates several important Python concepts:

* `json` — to store and read student data

* `os` — to check whether the student file exists

* Functions — to organize different operations

* Lists — to store multiple student records

* Dictionaries — to store individual student information

* `input()` — to get information from the user

* `int()` — to convert input into integers

* `try` / `except` — to handle errors

* `if`, `elif`, and `else` — to make decisions

* `for` loops — to search through student records

* `.append()` — to add a student

* `.remove()` — to delete a student

* `.strip()` — to remove unnecessary spaces

* `.lower()` — to handle confirmation input

* `return` — to exit functions

* `break` — to exit the main loop

* `json.dump()` — to save data

* `json.load()` — to read data

## 💻 Code

```python
import json
import os

FILE_NAME = "students.json"


def load_students():
    try:
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Error reading student file.")
        return []


def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

    except OSError:
        print("Error saving student records.")


def add_student():
    students = load_students()

    try:
        student_id = int(input("Enter Student ID: "))

        for student in students:
            if student["id"] == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter Student Name: ").strip()

        if name == "":
            print("Name cannot be empty.")
            return

        age = int(input("Enter Age: "))

        if age <= 0:
            print("Age must be greater than 0.")
            return

        course = input("Enter Course/Class: ").strip()

        if course == "":
            print("Course cannot be empty.")
            return

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        save_students(students)

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter numbers where required.")


def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n------ STUDENT RECORDS ------")

    for student in students:
        print("ID     :", student["id"])
        print("Name   :", student["name"])
        print("Age    :", student["age"])
        print("Course :", student["course"])
        print("-----------------------------")


def search_student():
    students = load_students()

    try:
        student_id = int(input("Enter Student ID to search: "))

        for student in students:
            if student["id"] == student_id:
                print("\nStudent Found!")
                print("ID     :", student["id"])
                print("Name   :", student["name"])
                print("Age    :", student["age"])
                print("Course :", student["course"])
                return

        print("Student not found.")

    except ValueError:
        print("Invalid ID! Please enter a number.")


def update_student():
    students = load_students()

    try:
        student_id = int(input("Enter Student ID to update: "))

        for student in students:
            if student["id"] == student_id:

                print("\nLeave a field empty to keep the old value.")

                name = input(
                    f"Enter new name ({student['name']}): "
                ).strip()

                age = input(
                    f"Enter new age ({student['age']}): "
                ).strip()

                course = input(
                    f"Enter new course ({student['course']}): "
                ).strip()

                if name:
                    student["name"] = name

                if age:
                    try:
                        new_age = int(age)

                        if new_age <= 0:
                            print("Age must be greater than 0.")
                            return

                        student["age"] = new_age

                    except ValueError:
                        print("Invalid age.")
                        return

                if course:
                    student["course"] = course

                save_students(students)

                print("Student record updated successfully!")
                return

        print("Student not found.")

    except ValueError:
        print("Invalid ID! Please enter a number.")


def delete_student():
    students = load_students()

    try:
        student_id = int(input("Enter Student ID to delete: "))

        for student in students:
            if student["id"] == student_id:

                confirm = input(
                    "Are you sure you want to delete this student? (y/n): "
                ).lower()

                if confirm == "y":
                    students.remove(student)
                    save_students(students)
                    print("Student deleted successfully!")
                else:
                    print("Delete cancelled.")

                return

        print("Student not found.")

    except ValueError:
        print("Invalid ID! Please enter a number.")


def main():
    while True:

        print("\n================================")
        print(" STUDENT RECORD MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Record Management System.")
            break

        else:
            print("Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    main()
```

## 🖥️ Example

### Main Menu

```text
================================
 STUDENT RECORD MANAGEMENT SYSTEM
================================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
================================
Enter your choice (1-6):
```

### Add Student

```text
Enter your choice (1-6): 1

Enter Student ID: 101
Enter Student Name: Muhammad Rehan
Enter Age: 16
Enter Course/Class: Python

Student added successfully!
```

### View Students

```text
------ STUDENT RECORDS ------

ID     : 101
Name   : Muhammad Rehan
Age    : 16
Course : Python
-----------------------------
```

### Search Student

```text
Enter Student ID to search: 101

Student Found!
ID     : 101
Name   : Muhammad Rehan
Age    : 16
Course : Python
```

### Update Student

```text
Enter Student ID to update: 101

Leave a field empty to keep the old value.

Enter new name (Muhammad Rehan):
Enter new age (16): 17
Enter new course (Python): Advanced Python

Student record updated successfully!
```

### Delete Student

```text
Enter Student ID to delete: 101

Are you sure you want to delete this student? (y/n): y

Student deleted successfully!
```

## 💾 JSON File Storage

The program stores student information in:

```text
students.json
```

Example:

```json
[
    {
        "id": 101,
        "name": "Muhammad Rehan",
        "age": 16,
        "course": "Python"
    }
]
```

This means the student information is **saved permanently** instead of disappearing when the program closes.

## 📂 Project Structure

```text
Student-Record-Management-System/

│
├── student_record_management.py
├── students.json
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 3. Open the Project Folder

```bash
cd Student-Record-Management-System
```

### 4. Run the Program

```bash
python student_record_management.py
```

The `students.json` file will be created automatically when student records are saved.

## 🎯 Purpose

This project was created as a **Python practice project** to move from basic programs toward real-world applications.

It provides practice with:

* Functions
* Lists
* Dictionaries
* JSON
* File handling
* Exception handling
* Loops
* Conditions
* User input
* Data validation
* CRUD operations

### CRUD Operations

This project also introduces the basic **CRUD** concept:

| Operation      | Program Feature     |
| -------------- | ------------------- |
| **C — Create** | Add Student         |
| **R — Read**   | View/Search Student |
| **U — Update** | Update Student      |
| **D — Delete** | Delete Student      |

## 🚀 Future Improvements

The project can be improved by adding:

* 📊 Student marks and grades

* 📅 Attendance management

* 📧 Student email

* 📱 Phone numbers

* 🔎 Search by name

* 📈 Student result reports

* 🔐 Admin login system

* 📁 Backup system

* 🖥️ Graphical User Interface (GUI)

* 🗄️ Database support such as SQLite or MySQL

## 👨‍💻 Author

**Muhammad Rehan**

> Beginner Python Developer | Learning Programming Step by Step

---

⭐ If you find this project useful, feel free to give it a star!
