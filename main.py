
import json
import os

FILE_NAME = "students.json"


# -------------------------------
# Load students from file
# -------------------------------
def load_students():
    try:
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Error reading student file.")
        return []


# -------------------------------
# Save students to file
# -------------------------------
def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

    except OSError:
        print("Error saving student records.")


# -------------------------------
# Add Student
# -------------------------------
def add_student():
    students = load_students()

    try:
        student_id = int(input("Enter Student ID: "))

        # Check duplicate ID
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


# -------------------------------
# View Students
# -------------------------------
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


# -------------------------------
# Search Student
# -------------------------------
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


# -------------------------------
# Update Student
# -------------------------------
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


# -------------------------------
# Delete Student
# -------------------------------
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


# -------------------------------
# Main Menu
# -------------------------------
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


# -------------------------------
# Start Program
# -------------------------------
if __name__ == "__main__":
    main()      