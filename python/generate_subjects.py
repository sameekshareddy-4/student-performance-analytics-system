import pandas as pd
import os

subjects = [
    # Computer Science
    ("CS101", "Programming Fundamentals", "Computer Science", 4),
    ("CS102", "Data Structures", "Computer Science", 4),
    ("CS103", "DBMS", "Computer Science", 4),
    ("CS104", "Operating Systems", "Computer Science", 4),
    ("CS105", "Computer Networks", "Computer Science", 3),

    # Artificial Intelligence
    ("AI101", "Python for AI", "Artificial Intelligence", 4),
    ("AI102", "Machine Learning", "Artificial Intelligence", 4),
    ("AI103", "Deep Learning", "Artificial Intelligence", 4),
    ("AI104", "Computer Vision", "Artificial Intelligence", 3),
    ("AI105", "Natural Language Processing", "Artificial Intelligence", 3),

    # Data Science
    ("DS101", "Statistics", "Data Science", 4),
    ("DS102", "Data Visualization", "Data Science", 3),
    ("DS103", "Data Mining", "Data Science", 4),
    ("DS104", "Big Data", "Data Science", 4),
    ("DS105", "Data Analytics", "Data Science", 4),

    # Information Technology
    ("IT101", "Web Technologies", "Information Technology", 4),
    ("IT102", "Cloud Computing", "Information Technology", 4),
    ("IT103", "Cyber Security", "Information Technology", 4),
    ("IT104", "Software Engineering", "Information Technology", 3),
    ("IT105", "Mobile Computing", "Information Technology", 3),

    # Electronics
    ("EC101", "Digital Electronics", "Electronics", 4),
    ("EC102", "Microprocessors", "Electronics", 4),
    ("EC103", "Signals & Systems", "Electronics", 4),
    ("EC104", "Embedded Systems", "Electronics", 3),
    ("EC105", "Communication Systems", "Electronics", 3),

    # Mechanical
    ("ME101", "Engineering Mechanics", "Mechanical", 4),
    ("ME102", "Thermodynamics", "Mechanical", 4),
    ("ME103", "Manufacturing", "Mechanical", 4),
    ("ME104", "Fluid Mechanics", "Mechanical", 3),
    ("ME105", "Machine Design", "Mechanical", 3),

    # Civil
    ("CV101", "Surveying", "Civil", 4),
    ("CV102", "Structural Analysis", "Civil", 4),
    ("CV103", "Construction Materials", "Civil", 4),
    ("CV104", "Transportation Engineering", "Civil", 3),
    ("CV105", "Environmental Engineering", "Civil", 3),

    # Business Analytics
    ("BA101", "Business Statistics", "Business Analytics", 4),
    ("BA102", "Excel for Analytics", "Business Analytics", 3),
    ("BA103", "Power BI", "Business Analytics", 4),
    ("BA104", "SQL for Analytics", "Business Analytics", 4),
    ("BA105", "Business Intelligence", "Business Analytics", 4)
]

df = pd.DataFrame(
    subjects,
    columns=["Subject_ID", "Subject_Name", "Department", "Credits"]
)

df.to_csv("data/raw/subjects.csv", index=False)

print(df)
print("\nSubjects Dataset Created Successfully!")