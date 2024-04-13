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
