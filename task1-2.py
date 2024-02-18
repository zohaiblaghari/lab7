def get_student_data(num_students):
    student_data = {}
    for i in range(1, num_students + 1):
        name = input(f"Enter the name of student {i}:")
        marks = float(input(f"Enter the marks obtained by {name}:"))
        if name in student_data:
            print(f"Warning: {name} already exists in the student data.")
            overwrite = input("Do you want to overwrite the existing data? (yes/no):").lower()
            if overwrite == "yes":
                student_data[name] = marks
                print(f"Data for {name} updated successfullu.")
            else:
                print(f"Data for {name} not updated.")
        else:
            student_data[name] = marks
    return student_data

if __name__ == "__main__":
    num_students = 10
    student_marks = get_student_data(num_students)
    print("Student Data:")
    for name, marks in student_marks.items():
        print(f"{name}: {marks}")