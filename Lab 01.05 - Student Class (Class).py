class Student:
    def __init__(self, name, gender, age, student_id, gpa):
        self.name = name
        self.gender = gender
        self.age = age
        self.student_id = student_id
        self.gpa = gpa

    def display_info(self):
        prefix = "Mr" if self.gender.lower() == "male" else "Miss"
        return f"{prefix} {self.name} ({self.age}) ID: {self.student_id} GPA {self.gpa:.2f}"
def main():
    students = []
    for _ in range(3):
        name, gender = input(), input()
        age, student_id, gpa = int(input()), input(), float(input())
        students.append(Student(name, gender, age, student_id, gpa))
    search_id = input()
    for student in students:
        if student.student_id == search_id:
            print(student.display_info())
            break
    else:
        print("Student not found")
main()
