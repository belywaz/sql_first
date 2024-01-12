from pathlib import Path
import sqlite3
import os



Path = os.path.dirname(__file__) + os.sep
con = sqlite3.connect(Path + "students.db")

cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    major TEXT
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS course (
                    course_id INTEGER PRIMARY KEY,
                    course_name TEXT
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS students_course (
                    student_id INTEGER,
                    course_id INTEGER,
                    FOREIGN KEY (course_id) REFERENCES course(course_id),
                    FOREIGN KEY (student_id) REFERENCES students(id)
                )''')