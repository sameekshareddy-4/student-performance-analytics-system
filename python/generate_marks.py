import pandas as pd
import random

# Load datasets
students = pd.read_csv("data/raw/students.csv")
subjects = pd.read_csv("data/raw/subjects.csv")

marks_data = []

grade_points = {
    "A+": 10,
    "A": 9,
    "B+": 8,
    "B": 7,
    "C": 6,
    "D": 5,
    "F": 0
}

for _, student in students.iterrows():

    dept_subjects = subjects[
        subjects["Department"] == student["Department"]
    ]

    for _, subject in dept_subjects.iterrows():

        attendance = random.randint(60, 100)

        internal = random.randint(15, 30)

        external = random.randint(20, 70)

        final_marks = internal + external

        if final_marks >= 90:
            grade = "A+"
        elif final_marks >= 80:
            grade = "A"
        elif final_marks >= 70:
            grade = "B+"
        elif final_marks >= 60:
            grade = "B"
        elif final_marks >= 50:
            grade = "C"
        elif final_marks >= 40:
            grade = "D"
        else:
            grade = "F"

        pass_fail = "Pass" if final_marks >= 40 else "Fail"

        marks_data.append({

            "Student_ID": student["Student_ID"],

            "Department": student["Department"],

            "Semester": student["Semester"],

            "Subject_ID": subject["Subject_ID"],

            "Internal_Marks": internal,

            "External_Marks": external,

            "Final_Marks": final_marks,

            "Attendance": attendance,

            "Grade": grade,

            "Grade_Point": grade_points[grade],

            "Pass_Fail": pass_fail

        })

df = pd.DataFrame(marks_data)

df.to_csv("data/raw/marks.csv", index=False)

print(df.head())

print("\nMarks Dataset Created Successfully!")
print("Rows :", len(df))