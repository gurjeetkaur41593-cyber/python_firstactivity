# -------------------------------
# Patient Class
# -------------------------------
class Patient:
    def __init__(self, patient_id, first_name, last_name, age, gender, phone, address):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address

    def is_senior(self):
        return self.age > 65


# -------------------------------
# Doctor Class
# -------------------------------
class Doctor:
    def __init__(self, doctor_id, first_name, last_name, specialization):
        self.doctor_id = doctor_id
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization


# -------------------------------
# Clinic Class
# -------------------------------
class Clinic:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    # Requirement 1
    def list_senior_patients(self):
        print("Senior Patients (Age > 65):")
        for patient in self.patients:
            if patient.is_senior():
                print(vars(patient))

    # Requirement 2
    def count_ophthalmology_doctors(self):
        count = 0
        for doctor in self.doctors:
            if doctor.specialization.lower() == "ophthalmology":
                count += 1
        return count
    
    # Create clinic
clinic = Clinic()

# Add patients
clinic.add_patient(Patient(1, "John", "Smith", 70, "Male", "021123456", "Auckland"))
clinic.add_patient(Patient(2, "Mary", "Brown", 60, "Female", "021654321", "Wellington"))
clinic.add_patient(Patient(3, "David", "Lee", 72, "Male", "021987654", "Christchurch"))

# Add doctors
clinic.add_doctor(Doctor(1, "Sarah", "Wilson", "Ophthalmology"))
clinic.add_doctor(Doctor(2, "James", "Taylor", "Cardiology"))
clinic.add_doctor(Doctor(3, "Emma", "Clark", "Ophthalmology"))

# Display results
clinic.list_senior_patients()
print("Total Ophthalmology Doctors:", clinic.count_ophthalmology_doctors())
