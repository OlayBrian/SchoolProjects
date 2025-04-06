from student import Student
from student_repo import StudentRepository

repo = StudentRepository()  

class StudentService:
    def add_student(self, student_id, name, age, grade):
        if int(age) < 15 or int(grade) < 70:
            print("Invalid age or grade!")  
            return  
        repo.add_student(Student(student_id, name, age, grade))

    def get_students(self):
        return repo.get_students()

    def delete_student(self, student_id):
        repo.delete_student(student_id)
