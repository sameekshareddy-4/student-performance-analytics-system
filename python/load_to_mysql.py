import pandas as pd
import mysql.connector

# ------------------------------
# MySQL Connection
# ------------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sam4",
    database="student_analytics",
    port=3306
)

cursor = conn.cursor()

print("Connected to MySQL\n")

# ------------------------------
# Load CSV Files
# ------------------------------

students = pd.read_csv("data/raw/students.csv")
subjects = pd.read_csv("data/raw/subjects.csv")
marks = pd.read_csv("data/raw/marks.csv")
# Rearrange columns to match MySQL table
marks = marks[
    [
        "Student_ID",
        "Subject_ID",
        "Department",
        "Semester",
        "Internal_Marks",
        "External_Marks",
        "Final_Marks",
        "Attendance",
        "Grade",
        "Grade_Point",
        "Pass_Fail"
    ]
]

# ------------------------------
# Insert Students
# ------------------------------

student_sql = """
INSERT INTO students
(Student_ID, First_Name, Last_Name, Gender, Age, Department, Semester, City, State, Admission_Year)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

student_values = [
    tuple(row)
    for row in students.values
]

cursor.executemany(student_sql, student_values)
conn.commit()

print(f"Students Imported : {len(student_values)}")

# ------------------------------
# Insert Subjects
# ------------------------------

subject_sql = """
INSERT INTO subjects
(Subject_ID, Subject_Name, Department, Credits)
VALUES (%s,%s,%s,%s)
"""

subject_values = [
    tuple(row)
    for row in subjects.values
]

cursor.executemany(subject_sql, subject_values)
conn.commit()

print(f"Subjects Imported : {len(subject_values)}")

# ------------------------------
# Insert Marks
# ------------------------------

mark_sql = """
INSERT INTO marks
(Student_ID, Subject_ID, Department, Semester,
Internal_Marks, External_Marks, Final_Marks,
Attendance, Grade, Grade_Point, Pass_Fail)

VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

batch_size = 1000

rows = [
    tuple(row)
    for row in marks.values
]

for i in range(0, len(rows), batch_size):

    batch = rows[i:i+batch_size]

    cursor.executemany(mark_sql, batch)

    conn.commit()

    print(f"Imported {min(i+batch_size, len(rows))} / {len(rows)}")

print("\nAll data imported successfully!")

cursor.close()
conn.close()