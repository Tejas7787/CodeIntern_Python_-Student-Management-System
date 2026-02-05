import json
import os

FILE_NAME = "students.json"

# Load students from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add new student
def add_student(students):
    roll = input("Enter Roll No: ")
    
    for s in students:
        if s["roll"] == roll:
            print("❌ Student with this Roll No already exists!")
            return

    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })
    save_students(students)
    print("✅ Student added successfully!")

# Display all students
def display_students(students):
    if not students:
        print("⚠ No student records found.")
        return

    print("\nRoll No   Name                Marks")
    print("-" * 35)
    for s in students:
        print(f"{s['roll']:<9} {s['name']:<18} {s['marks']}")

# Search student
def search_student(students):
    roll = input("Enter Roll No to search: ")
    for s in students:
        if s["roll"] == roll:
            print("✅ Student Found:")
            print(s)
            return
    print("❌ Student not found.")

# Update student
def update_student(students):
    roll = input("Enter Roll No to update: ")
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["marks"] = input("Enter new marks: ")
            save_students(students)
            print("✅ Student updated successfully!")
            return
    print("❌ Student not found.")

# Delete student
def delete_student(students):
    roll = input("Enter Roll No to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_students(students)
            print("✅ Student deleted successfully!")
            return
    print("❌ Student not found.")

# Main Menu
def main():
    students = load_students()

    while True:
        print("\n📚 Student Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            search_student(students)
        elif choice == "5":
            display_students(students)
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
