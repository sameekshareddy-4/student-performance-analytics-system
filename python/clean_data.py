import pandas as pd

# Load datasets
students = pd.read_csv("data/raw/students.csv")
subjects = pd.read_csv("data/raw/subjects.csv")
marks = pd.read_csv("data/raw/marks.csv")

# Merge datasets
df = marks.merge(students, on=["Student_ID", "Department", "Semester"])

df = df.merge(
    subjects,
    on=["Subject_ID", "Department"],
    how="left"
)

# Calculate CGPA
cgpa = (
    df.groupby("Student_ID")["Grade_Point"]
    .mean()
    .round(2)
    .reset_index()
)

cgpa.rename(columns={"Grade_Point": "CGPA"}, inplace=True)

df = df.merge(cgpa, on="Student_ID")

# Performance Category
def performance(cgpa):

    if cgpa >= 9:
        return "Excellent"

    elif cgpa >= 8:
        return "Very Good"

    elif cgpa >= 7:
        return "Good"

    elif cgpa >= 6:
        return "Average"

    else:
        return "Poor"

df["Performance_Category"] = df["CGPA"].apply(performance)

# Attendance Category
def attendance_category(att):

    if att >= 90:
        return "Excellent"

    elif att >= 80:
        return "Good"

    elif att >= 70:
        return "Average"

    else:
        return "Poor"

df["Attendance_Category"] = df["Attendance"].apply(attendance_category)

# Save final dataset
df.to_csv("data/final/student_analytics.csv", index=False)

print(df.head())

print("\nFinal Dataset Created Successfully!")
print("Rows :", len(df))