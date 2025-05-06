print("\n\nSelect the option to continue:")

while True:
    print("\n1) Add student\n2) Update Student\n3) Remove Student\n4) List Students\n5) Exit Program\n")
    

    if choice == 1:
        add_student()
    elif choice == 2:
        update_student()
    elif choice == 3:
        remove_student()
    elif choice == 4:
        list_students()
    elif choice == 5:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice. Please select a valid option.\n")

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    class_name = input("Enter class: ")
    age = input("Enter age: ")
    phone = input("Enter phone number: ")
    students.append({
        'Name': name,
        'Roll': roll,
        'Class': class_name,
        'Age': age,
        'Phone': phone
    })
    print("Student added successfully.\n")

def update_student():
    name = input("Enter name number of student to update: ")
    for student in students:
        if student['name'] == name:
            student['roll'] = input("Enter new roll: ")
            student['Class'] = input("Enter new class: ")
            student['Age'] = input("Enter new age: ")
            student['Phone'] = input("Enter new phone number: ")
            print("Student information updated.\n")
            return
    print("Student not found.\n")

def remove_student():
    name = input("Enter the name of the student to remove: ")
    global students
    students = [s for s in students if s['Name'].lower() != name.lower()]
    print("Student removed if existed.\n")

def list_students():
    if not students:
        print("No student records found.\n")
        return
    for idx, student in enumerate(students, start=1):
        print(f"\nStudent {idx}:")
        for key, value in student.items():
            print(f"{key}: {value}")
    print()


