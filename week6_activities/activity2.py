class StudentManager:
    def __init__(self):
        # Dictionary: student ID -> student name
        self.students = {}

        # Dictionary: student ID -> MSE800 score
        self.mse800_scores = {}

    def add_student(self, student_id, name, score):
        self.students[student_id] = name
        self.mse800_scores[student_id] = score

    def get_passed_students(self):
        """
        Combines both dictionaries and returns
        a new dictionary of students who passed (score >= 50)
        """
        passed_students = {}

        for student_id, score in self.mse800_scores.items():
            if score >= 50:
                passed_students[student_id] = {
                    "name": self.students[student_id],
                    "score": score
                }

        return passed_students

    def display_passed_students(self):
        passed = self.get_passed_students()
        print("Passed Students:")
        for student_id, details in passed.items():
            print(
                f"ID: {student_id}, "
                f"Name: {details['name']}, "
                f"MSE800 Score: {details['score']}"
            )


# -------- Main Program --------
manager = StudentManager()

# Adding five students
manager.add_student("S001", "Amarjeet Singh", 78)
manager.add_student("S002", "Sharanpal Kaur", 85)
manager.add_student("S003", "Jaskaran Kaur", 42)
manager.add_student("S004", "Gurpreet Singh", 74)
manager.add_student("S005", "Navdeep Kaur", 90)

# Display passed students only
manager.display_passed_students()
