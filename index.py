import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

class Admin:
    def __init__(self, db):
        self.db = db
    
    def login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        # Check if username and password are correct
        # Dummy check for demonstration
        if username == "admin" and password == "adminpassword":
            self.menu()
        else:
            print("Invalid username or password")
    
    def menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. View Doctors")
            print("2. Add Doctor")
            print("3. Update Doctor")
            print("4. Delete Doctor")
            print("5. View Patients")
            print("6. Delete Patient")
            print("7. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_doctors()
            elif choice == "2":
                self.add_doctor()
            elif choice == "3":
                self.update_doctor()
            elif choice == "4":
                self.delete_doctor()
            elif choice == "5":
                self.view_patients()
            elif choice == "6":
                self.delete_patient()
            elif choice == "7":
                break
            else:
                print("Invalid choice")
    
    def view_doctors(self):
        self.db.cursor.execute("SELECT * FROM doctors")
        doctors = self.db.cursor.fetchall()
        if not doctors:
            print("No doctors found")
        else:
            print("Doctors:")
            for doctor in doctors:
                print(doctor)
    
    def add_doctor(self):
        name = input("Enter doctor's name: ")
        password = input("Enter doctor's password: ")
        specialist = input("Enter doctor's specialist: ")
        available_hours = input("Enter doctor's available hours: ")
        self.db.cursor.execute("INSERT INTO doctors (name, password, specialist, available_hours) VALUES (%s, %s, %s, %s)", (name, password, specialist, available_hours))
        self.db.connection.commit()
        print("Doctor added successfully")
    
    def update_doctor(self):
        self.view_doctors()
        doctor_id = int(input("Enter doctor ID to update: "))
        available_hours = input("Enter updated available hours: ")
        self.db.cursor.execute("UPDATE doctors SET available_hours = %s WHERE id = %s", (available_hours, doctor_id))
        self.db.connection.commit()
        print("Doctor updated successfully")
    
    def delete_doctor(self):
        self.view_doctors()
        doctor_id = int(input("Enter doctor ID to delete: "))
        self.db.cursor.execute("DELETE FROM doctors WHERE id = %s", (doctor_id,))
        self.db.connection.commit()
        print("Doctor deleted successfully")

    # view patients done by Irielle Irakoze
        
    def view_patients(self):
        self.db.cursor.execute("SELECT * FROM patients")
        patients = self.db.cursor.fetchall()
        if not patients:
            print("No patients found")
        else:
            print("Patients:")
            for patient in patients:
                print(patient)
    
    def delete_patient(self):
        self.view_patients()
        patient_id = int(input("Enter patient ID to delete: "))
        self.db.cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
        self.db.connection.commit()
        print("Patient deleted successfully")
        
class Patient:
    def __init__(self, db):
        self.db = db
    
    def menu(self):
        while True:
            print("\nPatient Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                break
            else:
                print("Invalid choice")
    
    
    def dashboard(self, patient):
        print("Welcome,", patient[1])
        while True:
            print("\nPatient Dashboard:")
            print("1. Search Doctor by Specialist")
            print("2. Book Appointment")
            print("3. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.search_doctor_by_specialist()
            elif choice == "2":
                self.book_appointment(patient)
            elif choice == "3":
                break
            else:
                print("Invalid choice")
                
    def register(self):
        name = input("Enter your name: ")
        username = input("Enter desired username: ")
        password = input("Enter password: ")
        self.db.cursor.execute("INSERT INTO patients (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
        self.db.connection.commit()
        print("Patient registered successfully")
    
    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.db.cursor.execute("SELECT * FROM patients WHERE username = %s AND password = %s", (username, password))
        patient = self.db.cursor.fetchone()
        if patient:
            self.dashboard(patient)
        else:
            print("Invalid username or password")

class Doctor:
    def __init__(self, db):
        self.db = db
    
    def menu(self):
        while True:
            print("\nDoctor Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                break
            else:
                print("Invalid choice")
    
    
    def dashboard(self, doctor):
        print("Welcome,", doctor[1])
        while True:
            print("\nDoctor Dashboard:")
            print("1. View Appointments")
            print("2. Approve/Reject Appointment")
            print("3. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_appointments()
            elif choice == "2":
                self.manage_appointments()
            elif choice == "3":
                break
            else:
                print("Invalid choice")
    
    def view_appointments(self):
        self.db.cursor.execute("SELECT * FROM appointments WHERE doctor_id = %s", (doctor[0],))
        appointments = self.db.cursor.fetchall()
        if not appointments:
            print("No appointments found")
        else:
            print("Appointments:")
            for appointment in appointments:
                print(appointment)
    
    def manage_appointments(self):
        appointment_id = input("Enter appointment ID to approve/reject: ")
        status = input("Enter status (Approved/Rejected): ")
        self.db.cursor.execute("UPDATE appointments SET status = %s WHERE id = %s", (status, appointment_id))
        self.db.connection.commit()
        print("Appointment status updated successfully")

def main():
    db = Database("localhost", "root", "Boaz@123", "medical_appointment")
    print("Welcome to the Medical Appointment System")
    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. Patient Menu")
        print("3. Doctor Menu")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            admin = Admin(db)
            admin.login()
        elif choice == "2":
            patient = Patient(db)
            patient.menu()
        elif choice == "3":
            doctor = Doctor(db)
            doctor.menu()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
