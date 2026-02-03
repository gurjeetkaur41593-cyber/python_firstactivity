import sqlite3


class StudentDatabase:
    def __init__(self, db_name="students.db"):
        # Connect to SQLite database
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Create Student table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Student (
                student_id TEXT PRIMARY KEY,
                student_name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        """)
        self.connection.commit()

    def add_student(self, student_id, student_name, score):
        # Insert student record into database
        self.cursor.execute("""
            INSERT OR REPLACE INTO Student (student_id, student_name, score)
            VALUES (?, ?, ?)
        """, (student_id, student_name, score))
        self.connection.commit()

    def get_top_three_students(self):
        # SQL query to retrieve top 3 students by score
        self.cursor.execute("""
            SELECT student_id, student_name, score
            FROM Student
            ORDER BY score DESC
            LIMIT 3
        """)
        return self.cursor.fetchall()

    def display_top_three_students(self):
        top_students = self.get_top_three_students()
        print("Top 3 Students Based on MSE800 Score:")
        for student in top_students:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Score: {student[2]}"
            )

    def close_connection(self):
        self.connection.close()


# -------- Main Program --------
db = StudentDatabase()

# Adding students
db.add_student("S001", "Amarjeet Singh", 78)
db.add_student("S002", "Sharanpal Kaur", 85)
db.add_student("S003", "Jaskaran Kaur", 42)
db.add_student("S004", "Gurpreet Singh", 74)
db.add_student("S005", "Navdeep Kaur", 90)

# Display top three students
db.display_top_three_students()

# Close database connection
db.close_connection()
