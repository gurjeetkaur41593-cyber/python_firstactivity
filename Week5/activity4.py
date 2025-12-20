# ----------------------------------
# Base Class: Person
# ----------------------------------
class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def display_info(self):
        # Common method for all persons
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")


# ----------------------------------
# Child Class: Student (inherits Person)
# ----------------------------------
class Student(Person):
    def __init__(self, student_id, name):
        # Call the constructor of Person
        super().__init__(student_id, name)
        self.student_id = student_id

    def display_info(self):
        print("Student Information:")
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print("----------------------")


# ----------------------------------
# Child Class: Staff (inherits Person)
# ----------------------------------
class Staff(Person):
    def __init__(self, staff_id, name, tax_num):
        # Call the constructor of Person
        super().__init__(staff_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display_info(self):
        print("Staff Information:")
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Tax Number: {self.tax_num}")


# ----------------------------------
# Child Class: General (inherits Staff)
# ----------------------------------
class General(Staff):
    def __init__(self, staff_id, name, tax_num, rate_of_pay):
        # Call the constructor of Staff
        super().__init__(staff_id, name, tax_num)
        self.rate_of_pay = rate_of_pay

    def display_info(self):
        print("General Staff Information:")
        super().display_info()
        print(f"Rate of Pay: {self.rate_of_pay}")
        print("---------------------------")


# ----------------------------------
# Child Class: Academic (inherits Staff)
# ----------------------------------
class Academic(Staff):
    def __init__(self, staff_id, name, tax_num, publications):
        # Call the constructor of Staff
        super().__init__(staff_id, name, tax_num)
        self.publications = publications

    def display_info(self):
        print("Academic Staff Information:")
        super().display_info()
        print(f"Publications: {self.publications}")
        print("----------------------------")


# ----------------------------------
# Main Program (Object Creation)
# ----------------------------------

# Create a student object
student1 = Student(101, "Alice Brown")

# Create a general staff object
general_staff1 = General(201, "John Smith", "TX12345", 30.50)

# Create an academic staff object
academic_staff1 = Academic(301, "Dr Emma Wilson", "TX98765", 15)

# Display details
student1.display_info()
general_staff1.display_info()
academic_staff1.display_info()
