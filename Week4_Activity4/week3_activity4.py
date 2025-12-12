# -------------------------------
# OOP MODEL BASED ON THE ERD

# This program is based on a small university setup where students join courses and teachers teach them. We created classes for students, teachers, and courses to represent these real things. The Enrollment class connects a student to a course, while the Teaching class connects a teacher to a course. After adding some sample students, teachers, and courses, the program can answer basic questions. For example, it can count how many students are enrolled in MSE800 or show which teachers are teaching MSE801. This scenario shows how OOP helps us organise and work with data just like a real university system.

# -------------------------------

# Class to represent a Student
class Student:
    def __init__(self, student_id, first_name, last_name, email):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

# Class to represent a Teacher
class Teacher:
    def __init__(self, teacher_id, first_name, last_name, address):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

# Class to represent a Course
class Course:
    def __init__(self, course_id, course_name, duration):
        self.course_id = course_id
        self.course_name = course_name
        self.duration = duration

# Class to handle enrollments (Student → Course)
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

# Class to handle teaching assignments (Teacher → Course)
class Teaching:
    def __init__(self, teacher, course):
        self.teacher = teacher
        self.course = course


# ---------------------------------------
# SAMPLE DATA BASED ON YOUR DIAGRAM
# ---------------------------------------

# Create students
s1 = Student(1, "Gurjeet", "Kaur", "gurjeet@example.com")
s2 = Student(2, "Parul", "Parul", "parul@example.com")
s3 = Student(3, "Nancy", "Nancy", "nancy@example.com")

# Create teachers
t1 = Teacher(1, "Arun", "Kumar", "Auckland")
t2 = Teacher(2, "Dr", "Mohammad", "Wellington")
t3 = Teacher(3, "Savita", "Bai", "Hamilton")

# Create courses
c1 = Course("MSE800", "Professional Software Engineering", "10 weeks")
c2 = Course("MSE801", "Quantum Computing", "12 weeks")
c3 = Course("MSE802", "Research Methods", "15 weeks")

# ---------------------------------------
# Create Enrollment relationships
# ---------------------------------------
enrollments = [
    Enrollment(s1, c1),
    Enrollment(s2, c2),
    Enrollment(s3, c3)
]

# ---------------------------------------
# Create Teaching relationships
# ---------------------------------------
teaching_assignments = [
    Teaching(t1, c2),
    Teaching(t2, c2),
    Teaching(t3, c3)
]


# ---------------------------------------
# FUNCTION 1: COUNT STUDENTS ENROLLED IN MSE800
# ---------------------------------------
def count_students_in_mse800():
    count = 0
    for enroll in enrollments:
        # Compare course ID with "MSE800"
        if enroll.course.course_id == "MSE800":
            count += 1
    return count


# ---------------------------------------
# FUNCTION 2: LIST TEACHERS TEACHING MSE801
# ---------------------------------------
def list_teachers_for_mse801():
    teacher_names = []
    for teach in teaching_assignments:
        # Check if teacher teaches MSE801
        if teach.course.course_id == "MSE801":
            full_name = teach.teacher.first_name + " " + teach.teacher.last_name
            teacher_names.append(full_name)
    return teacher_names


# ---------------------------------------
# MAIN EXECUTION
# ---------------------------------------

print("---- RESULTS ----")

# Output how many students enrolled in MSE800
print("Number of students enrolled in MSE800:",
      count_students_in_mse800())

# Output teachers who teach MSE801
teachers_mse801 = list_teachers_for_mse801()
print("\nTeachers teaching MSE801:")
for name in teachers_mse801:
    print("-", name)
