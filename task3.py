def get_student_data(num_students):
    student_data = {}
    for i in range(1, num_students + 1):
        name = input(f"Enter the name of student {i}:")
        marks = float(input(f"Enter the marks obtained by {name}:"))
        student_data[i] = {'name': name, 'marks': marks}
    return student_data

if __name__ == "__main__":
    num_students = 10
    student_marks = get_student_data(num_students)
    print("Student Data:")
    for student_id, data in student_marks.items():
        print(f"Student ID: {student_id}, Name: {data['name']}, Marks: {data['marks']}")