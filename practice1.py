def input_students(num_students):
    '''dùng list để lưu trữ thông tin bởi vì list có thể lưu trữ đc cả dict và everything'''
    students = []
    for i in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        """dùng vòng lặp for lặp lại các bước thêm và điền thông tin vào list bằng hàm có sẵn của python append"""
        students.append({"id": student_id, "name": name, "dob": dob, "marks": {}})
    return students

def input_courses(num_courses):
    courses = []
    for i in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append({"id": course_id, "name": name})
    return courses

def input_marks(students, courses):
    course_id = input("Enter course ID to input marks: ")
    """python giản tiện hơn C hay C++ hay ngôn ngữ khác vì có thể dùng for kiểu này truy cập trực tiếp vào list vừa nhập thông tin vào"""
    for student in students:
        """dùng f"" python có cái này khác hay vì có thể dễ dàng dùng ngôn ngữ thực để nói"""
        marks = float(input(f"Enter marks for {student['name']} in {course_id}: "))
        student['marks'][course_id] = marks

def list_courses(courses):
    ''' dùng 1 hàm để trả về danh sách khóa học '''
    print("List of Courses:")
    for course in courses:
        print(f"{course['id']}: {course['name']}")

def list_students(students):
    ''' dùng 1 hàm để trả về danh sách học sinh'''
    print("List of Students:")
    for student in students:
        print(f"{student['id']}: {student['name']}")

def show_student_marks(students):
    student_id = input("Enter student ID to show marks: ")
    for student in students:
        '''kiểm tra xem id nhập ngoài có trùng với id của học sinh trong list không
        nếu có nó sẽ input tên học sinh và in ra điểm'''
        if student['id'] == student_id:
            print(f"Student: {student['name']}")
            for course_id, marks in student['marks'].items():
                """dùng .items() để trả về 1 cặp giá trị 
                tôi định dùng enumerate()"""
                
                print(f"Course: {course_id}, Marks: {marks}")
            return 0
    print("Student not found.")

def main():
    num_students = int(input("Enter number of students in the class: "))
    students = input_students(num_students)

    num_courses = int(input("Enter number of courses: "))
    courses = input_courses(num_courses)

    while True:
        print("\nOptions:")
        print("1. Input marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a given course")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            input_marks(students, courses)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            show_student_marks(students)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()