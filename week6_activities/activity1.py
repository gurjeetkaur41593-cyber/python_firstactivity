class StudentManager:
    def __init__(self):
        # Dictionary to store student ID and name
        self.students = {}

        # Dictionary to store student ID and MSE800 score
        self.mse800_scores = {}

    def add_student(self, student_id, name, score):
        self.students[student_id] = name
        self.mse800_scores[student_id] = score

    def display_students(self):
        print("Student Details:")
        for student_id in self.students:
            print(
                f"ID: {student_id}, "
                f"Name: {self.students[student_id]}, "
                f"MSE800 Score: {self.mse800_scores[student_id]}"
            )


# -------- Main Program --------
manager = StudentManager()

# Adding five students
manager.add_student("S001", "Amarjeet Singh", 78)
manager.add_student("S002", "Sharanpal Kaur", 85)
manager.add_student("S003", "Jaskaran Kaur", 82)
manager.add_student("S004", "Gurpreet Singh", 74)
manager.add_student("S005", "Navdeep Kaur", 90)

# Display all students
manager.display_students()
