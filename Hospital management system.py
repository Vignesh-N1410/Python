from abc import ABC, abstractmethod
import json

class Person(ABC):
    def __init__(self,name,age,phone):
        self.__name = name
        self.__age = age
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    @abstractmethod
    def display_details(self):
        pass

class Patient(Person):
    def __init__(self,name,age,phone,patient_id,disease,admission_date):
        super().__init__(name,age,phone)
        self.__patient_id = patient_id
        self.__disease = disease
        self.__admission_date = admission_date

    def get_patient_id(self):
        return self.__patient_id

    def get_disease(self):
        return self.__disease

    def get_admission_date(self):
        return self.__admission_date

    def display_details(self):
        print(f"The Patient ID is {self.get_patient_id()}\n"
              f"The patient name is {self.get_name()}\n"
              f"The patient age is {self.get_age()}\n"
              f"The disease is {self.get_disease()}\n"
              f"Admission date is {self.get_admission_date()}\n"
              f"Contact number is {self.get_phone()}\n")

class Doctor(Person):
    def __init__(self, name, age, phone, doctor_id, specialization, availability):
        super().__init__(name,age,phone)
        self.__doctor_id = doctor_id
        self.__specialization = specialization
        self.__availability = availability

    def get_doctor_id(self):
        return self.__doctor_id

    def get_specialization(self):
        return self.__specialization

    def get_availability(self):
        return self.__availability


    def display_details(self):
        print(f"The Doctor ID is : {self.get_doctor_id()}\n"
              f"Name of the Doctor is : {self.get_name()}\n"
              f"Age of the Doctor is : {self.get_age()}\n"
              f"specialised  in : {self.get_specialization()}\n"
              f"availability : {', '.join(self.get_availability())}\n"
              f"Contact details : {self.get_phone()}")

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date,status = "Scheduled"):
        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__doctor = doctor
        self.__date = date
        self.__status = status

    def get_appointment_id(self):
        return self.__appointment_id

    def get_status(self):
        return self.__status

    def get_patient(self):
        return self.__patient

    def get_doctor(self):
        return self.__doctor

    def get_date(self):
        return self.__date

    def set_status(self, status):
        if status.lower() in ["scheduled","completed","cancelled"]:
            self.__status = status
        else:
            raise ValueError("Invalid status value")

    def display_details(self):
        print(f"the appointment id : {self.get_appointment_id()}\n"
              f"The appointment date : {self.get_date()}\n"
              f"Status of the appointment : {self.get_status()}\n")
        print("The patient details:")
        self.get_patient().display_details()
        print("The doctor details:")
        self.get_doctor().display_details()

class Bill(ABC):
    def __init__(self, bill_id, appointment):
        self.__bill_id = bill_id
        self.__appointment = appointment

    def get_bill_id(self):
        return self.__bill_id

    def get_appointment(self):
        return self.__appointment

    @abstractmethod
    def calculate_bill(self):
        pass

    def display_bill(self):
        print(f"Bill ID is : {self.get_bill_id()}")
        print(f"Total Bill Amount : {self.calculate_bill()}\n"
              f"For the appointment : {self.get_appointment().get_appointment_id()}\n")

class GeneralBill(Bill):
    def __init__(self, bill_id, appointment,consultation_fee):
        super().__init__(bill_id,appointment)
        self.__consultation_fee = consultation_fee

    def calculate_bill(self):
        return self.__consultation_fee

class SurgeryBill(Bill):
    def __init__(self, bill_id, appointment,consultation_fee,surgery_cost):
        super().__init__(bill_id,appointment)
        self.__consultation_fee = consultation_fee
        self.__surgery_cost = surgery_cost

    def calculate_bill(self):
        return self.__consultation_fee + self.__surgery_cost

class Hospital:
    def __init__(self,hospital_name):
        self.__hospital_name = hospital_name
        self.__patients = []
        self.__doctors = []
        self.__appointments = []

    def add_patient(self,patient):
        self.__patients.append(patient)

    def add_doctor(self,doctor):
        self.__doctors.append(doctor)

    def book_appointment(self,appointment):
        self.__appointments.append(appointment)

    def display_all_patients(self):
        for patient in self.__patients:
            patient.display_details()

    def display_all_doctors(self):
        for doctor in self.__doctors:
            doctor.display_details()

    def display_all_appointments(self):
        for appointment in self.__appointments:
            appointment.display_details()

    def get_hospital_name(self):
        return self.__hospital_name

    def find_patients(self,id):
        for patient in self.__patients:
            if patient.get_patient_id() == id:
                return patient
        return None

    def get_patients(self):
        return self.__patients

    def get_doctors(self):
        return self.__doctors

    def get_appointments(self):
        return self.__appointments

    def find_doctors(self,id):
        for doctor in self.__doctors:
            if doctor.get_doctor_id() == id:
                return doctor
        return None

    def find_appointment(self, appointment_id):
        for appointment in self.__appointments:
            if appointment.get_appointment_id() == appointment_id:
                return appointment
        return None


class FileManager:
    def save_patients(self,patients,filename):
        data = []
        for p in patients:
            data.append({
                "patient_id": p.get_patient_id(),
                "name": p.get_name(),
                "age": p.get_age(),
                "phone": p.get_phone(),
                "disease": p.get_disease(),
                "admission_date": p.get_admission_date()
            })

        with open(filename,"w") as f:
            json.dump(data,f)

    def load_patients(self,filename):

        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_doctors(self,doctors,filename):
        data = []
        for d in doctors:
            data.append({
                "doctor_id": d.get_doctor_id(),
                "name": d.get_name(),
                "age": d.get_age(),
                "phone": d.get_phone(),
                "specialization": d.get_specialization(),
                "availability": d.get_availability()
            })

        with open(filename,"w") as f:
            json.dump(data,f)

    def load_doctors(self,filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_appointments(self, appointments, filename):
        data = []
        for a in appointments:
            data.append({
                "appointment_id": a.get_appointment_id(),
                "patient_id": a.get_patient().get_patient_id(),
                "doctor_id": a.get_doctor().get_doctor_id(),
                "date": a.get_date(),
                "status": a.get_status()
            })
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_appointments(self, filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

def main():
    hospital = Hospital("City Hospital")
    filemanager = FileManager()

    print("===== Hospital Management System =====")
    print("Do you want to load previous data?")
    print("1. Yes - Load Previous Data")
    print("2. No  - Start Fresh")

    load_choice = input("Enter choice: ")

    if load_choice == "1":
        # Load existing patients from file
        saved_patients = filemanager.load_patients("patients.json")
        for p in saved_patients:
            patient = Patient(
                p["name"], p["age"], p["phone"],
                p["patient_id"], p["disease"], p["admission_date"]
            )
            hospital.add_patient(patient)

        saved_doctors = filemanager.load_doctors("doctors.json")
        for d in saved_doctors:
            doctor = Doctor(
                d["name"], d["age"], d["phone"],
                d["doctor_id"], d["specialization"], d["availability"]
            )
            hospital.add_doctor(doctor)

        saved_appointments = filemanager.load_appointments("appointments.json")
        for a in saved_appointments:
            patient = hospital.find_patients(a["patient_id"])
            doctor = hospital.find_doctors(a["doctor_id"])
            appointment = Appointment(
                a["appointment_id"],
                patient,
                doctor,
                a["date"],
                a["status"]
            )
            hospital.book_appointment(appointment)

        print("Previous data loaded successfully!")

    else:
        print("Starting fresh!")

    while True:
        print("===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Book appointment")
        print("4. Display All Patients")
        print("5. Display All Doctors")
        print("6. Display All Appointments")
        print("7. Generate Bill")
        print("8. Save Data")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            # name, age, phone, patient_id, disease, admission_date
            name = input("Enter patient name: ")
            age = int(input("Enter  age: "))
            phone = input("Enter Contact_number: ")
            patient_id = input("Enter patient id: ")
            disease = input("Enter the disease you are diagnosing for :")
            admission_date = input("Enter the date of admission: ")

            patient = Patient(name, age, phone, patient_id, disease, admission_date)

            hospital.add_patient(patient)
            print("Patient added successfully!")

        elif choice == 2:
            # name, age, phone, doctor_id, specialization, availability
            name = input("Enter Doctor name: ")
            age = int(input("Enter  age: "))
            phone = input("Enter Contact_number: ")
            doctor_id = input("Enter Doctor ID: ")
            specialization = input("Enter specialization: ")
            availability = input("Enter availability (Comma separated): ").split(",")

            doctor = Doctor(name, age, phone, doctor_id, specialization, availability)

            hospital.add_doctor(doctor)
            print("Doctor added successfully!")

        elif choice == 3:
            patient_id = input("Enter patient id: ")
            patient = hospital.find_patients(patient_id)

            if patient is None:
                print("Patient not found!")
            else:
                doctor_id = input("Enter Doctor ID: ")
                doctor = hospital.find_doctors(doctor_id)

                if doctor is None:
                    print("Doctor not found!")
                else:
                    appointment_id = input("Enter Appointment ID: ")
                    date = input("Enter the date of appointment: ")

                    # appointment_id, patient, doctor, date, status = "Scheduled"
                    appointment = Appointment(appointment_id, patient, doctor, date)
                    hospital.book_appointment(appointment)
                    print("Appointment added successfully!")

        elif choice == 4:
            hospital.display_all_patients()

        elif choice == 5:
            hospital.display_all_doctors()

        elif choice == 6:
            hospital.display_all_appointments()

        elif choice == 7:
            print("1. General Bill")
            print("2. Surgery Bill")
            bill_type = input("Enter bill type: ")

            appointment_id = input("Enter Appointment ID: ")
            appointment = hospital.find_appointment(appointment_id)



            if appointment is None:
                print("Appointment ID Not found!")
            else:
                bill_id = input("Enter bill ID: ")
                if bill_type == "1":
                    consultation_fee = float(input("Enter consultation fee: "))
                    bill = GeneralBill(bill_id, appointment, consultation_fee)
                    bill.display_bill()

                elif bill_type == "2":
                    consultation_fee = float(input("Enter consultation fee: "))
                    surgery_cost = float(input("Enter surgery cost: "))
                    bill = SurgeryBill(bill_id, appointment, consultation_fee, surgery_cost)
                    bill.display_bill()

        elif choice == 8:

            filemanager.save_patients(hospital.get_patients(), "patients.json")
            filemanager.save_doctors(hospital.get_doctors(), "doctors.json")
            filemanager.save_appointments(hospital.get_appointments(), "appointments.json")
            print("Patients saved successfully!")

        elif choice == 9:

            filemanager.save_patients(hospital.get_patients(), "patients.json")
            filemanager.save_doctors(hospital.get_doctors(), "doctors.json")
            filemanager.save_appointments(hospital.get_appointments(), "appointments.json")
            print("Exiting...")
            break

if __name__ == "__main__":
    main()




















