import sqlite3
conn = sqlite3.connect("students.db")  
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade INTEGER)")
conn.commit()

class StudentRepository:
    def add_student(self, student):
        conn.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (student.id, student.name, student.age, student.grade))
        conn.commit()

    def get_students(self):
        return conn.execute("SELECT * FROM students").fetchall()

    def delete_student(self, student_id):
        conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
