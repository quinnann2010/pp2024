class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self, num_students):
        for i in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            self.students.append({"id": student_id, "name": name, "dob": dob, "marks": {}})

    def input_courses(self, num_courses):
        for i in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append({"id": course_id, "name": name})

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        for student in self.students:
            marks = float(input(f"Enter marks for {student['name']} in {course_id}: "))
            student['marks'][course_id] = marks

    def list_courses(self):
        print("List of Courses:")
        for course in self.courses:
            print(f"{course['id']}: {course['name']}")

    def list_students(self):
        print("List of Students:")
        for student in self.students:
            print(f"{student['id']}: {student['name']}")

    def show_student_marks(self):
        student_id = input("Enter student ID to show marks: ")
        for student in self.students:
            if student['id'] == student_id:
                print(f"Student: {student['name']}")
                for course_id, marks in student['marks'].items():
                    print(f"Course: {course_id}, Marks: {marks}")
                return
        print("Student not found.")

    def main(self):
        num_students = int(input("Enter number of students in the class: "))
        self.input_students(num_students)

        num_courses = int(input("Enter number of courses: "))
        self.input_courses(num_courses)

        while True:
            print("\nOptions:")
            print("1. Input marks for a course")
            print("2. List courses")
            print("3. List students")
            print("4. Show student marks for a given course")
            print("5. Quit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                self.input_marks()
            elif choice == '2':
                self.list_courses()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.show_student_marks()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    student_system = StudentManagementSystem()
    student_system.main()