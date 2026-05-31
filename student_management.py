students = {}

def add_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        print("Student ID already exists!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    students[sid] = {
        "Name": name,
        "Age": age,
        "Marks": marks
    }

    print("Student Added Successfully!")

def view_students():
    if len(students) == 0:
        print("No Student Records Found!")
        return

    print("\n----- Student Records -----")

    for sid, details in students.items():
        print(f"\nStudent ID : {sid}")
        print(f"Name       : {details['Name']}")
        print(f"Age        : {details['Age']}")
        print(f"Marks      : {details['Marks']}")

def search_student():
    sid = input("Enter Student ID to Search: ")

    if sid in students:
        print("\nStudent Found")
        print(f"Name  : {students[sid]['Name']}")
        print(f"Age   : {students[sid]['Age']}")
        print(f"Marks : {students[sid]['Marks']}")
    else:
        print("Student Not Found!")

def update_student():
    sid = input("Enter Student ID to Update: ")

    if sid in students:
        print("Enter New Details")

        students[sid]["Name"] = input("Name: ")
        students[sid]["Age"] = input("Age: ")
        students[sid]["Marks"] = input("Marks: ")

        print("Student Updated Successfully!")
    else:
        print("Student Not Found!")
def delete_student():
    sid = input("Enter Student ID to Delete: ")

    if sid in students:
        del students[sid]
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

while True:

    print("\n")
    print("===================================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

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
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")