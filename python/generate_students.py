from faker import Faker
import pandas as pd
import random
import os

fake = Faker("en_IN")

NUM_STUDENTS = 10000

departments = [
    "Computer Science",
    "Artificial Intelligence",
    "Data Science",
    "Information Technology",
    "Electronics",
    "Mechanical",
    "Civil",
    "Business Analytics"
]

city_state = {
    "Hyderabad": "Telangana",
    "Bengaluru": "Karnataka",
    "Chennai": "Tamil Nadu",
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Delhi": "Delhi",
    "Kolkata": "West Bengal",
    "Ahmedabad": "Gujarat",
    "Jaipur": "Rajasthan",
    "Lucknow": "Uttar Pradesh",
    "Visakhapatnam": "Andhra Pradesh",
    "Coimbatore": "Tamil Nadu",
    "Nagpur": "Maharashtra",
    "Bhopal": "Madhya Pradesh",
    "Kochi": "Kerala"
}

students = []

for i in range(1, NUM_STUDENTS + 1):

    admission_year = random.choice([2022, 2023, 2024, 2025])

    if admission_year == 2025:
        semester = random.randint(1, 2)
    elif admission_year == 2024:
        semester = random.randint(3, 4)
    elif admission_year == 2023:
        semester = random.randint(5, 6)
    else:
        semester = random.randint(7, 8)

    city = random.choice(list(city_state.keys()))

    department = random.choice(departments)

    # New Columns
    cgpa = round(random.uniform(5.5, 9.9), 2)

    scholarship = random.choices(
        ["Yes", "No"],
        weights=[25, 75]
    )[0]

    hostel = random.choice(
        ["Hosteller", "Day Scholar"]
    )

    fee_status = random.choices(
        ["Paid", "Pending"],
        weights=[90, 10]
    )[0]

    placement = (
        "Yes"
        if semester >= 6 and cgpa >= 7.0
        else "No"
    )

    students.append({

        "Student_ID": f"ST{i:05d}",

        "First_Name": fake.first_name(),

        "Last_Name": fake.last_name(),

        "Gender": random.choice(["Male", "Female"]),

        "Age": random.randint(18, 24),

        "Department": department,

        "Semester": semester,

        "City": city,

        "State": city_state[city],

        "Admission_Year": admission_year,

        "CGPA": cgpa,

        "Scholarship_Status": scholarship,

        "Hostel_Status": hostel,

        "Fee_Status": fee_status,

        "Placement_Eligible": placement

    })

df = pd.DataFrame(students)

os.makedirs("data/raw", exist_ok=True)

df.to_csv("data/raw/students.csv", index=False)

print(df.head())

print("\nDataset Created Successfully!")
print("Rows :", len(df))