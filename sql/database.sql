DROP DATABASE IF EXISTS student_analytics;

CREATE DATABASE student_analytics;

USE student_analytics;

CREATE TABLE students (

    Student_ID VARCHAR(10) PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Gender VARCHAR(10),
    Age INT,
    Department VARCHAR(100),
    Semester INT,
    City VARCHAR(100),
    State VARCHAR(100),
    Admission_Year INT,
    CGPA DECIMAL(3,2),
    Scholarship_Status VARCHAR(10),
    Hostel_Status VARCHAR(20),
    Fee_Status VARCHAR(20),
    Placement_Eligible VARCHAR(10)

);

CREATE TABLE subjects (

    Subject_ID VARCHAR(10) PRIMARY KEY,
    Subject_Name VARCHAR(100),
    Department VARCHAR(100),
    Credits INT

);

CREATE TABLE marks (

    Student_ID VARCHAR(10),
    Subject_ID VARCHAR(10),
    Department VARCHAR(100),
    Semester INT,
    Internal_Marks INT,
    External_Marks INT,
    Final_Marks INT,
    Attendance INT,
    Grade VARCHAR(5),
    Grade_Point INT,
    Pass_Fail VARCHAR(20),

    FOREIGN KEY (Student_ID)
        REFERENCES students(Student_ID),

    FOREIGN KEY (Subject_ID)
        REFERENCES subjects(Subject_ID)

);