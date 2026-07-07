CREATE DATABASE student_analytics;

USE student_analytics;

CREATE TABLE Students (

    Student_ID VARCHAR(10) PRIMARY KEY,

    First_Name VARCHAR(50),

    Last_Name VARCHAR(50),

    Gender VARCHAR(10),

    Age INT,

    Department VARCHAR(100),

    Semester INT,

    City VARCHAR(100),

    State VARCHAR(100),

    Admission_Year INT

);

CREATE TABLE Subjects (

    Subject_ID VARCHAR(10) PRIMARY KEY,

    Subject_Name VARCHAR(100),

    Department VARCHAR(100),

    Credits INT

);

CREATE TABLE Marks (

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

    FOREIGN KEY(Student_ID) REFERENCES Students(Student_ID),

    FOREIGN KEY(Subject_ID) REFERENCES Subjects(Subject_ID)

);