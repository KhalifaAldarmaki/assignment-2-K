#import python library
from collections import deque
from Doctor import Doctor
from Prescrption import Prescription

#Class of Hospital that has all functions calling    
class Hospital:
    def __init__(self):
        #dictionary used here for queue
        self.patients_queue = {}
        #deque method calling
        self.prescriptions_stack = deque()  
        #dictionary used here for patients record
        self.patients = {}
        #list used here for doctors record
        self.doctors = []
        #doctor details 
        self.doctors.append(Doctor("DR1", "Doctor Russell", "Cardiologist", "10 years", "Heart Surgery"))
        self.doctors.append(Doctor("DR2", "Doctor Ronaldo", "Orthopedic Surgeon", "8 years", "Bone Fractures"))
        self.doctors.append(Doctor("DM3", "Doctor Messy", "Neurologist", "12 years", "Brain Disorders"))
        self.doctors.append(Doctor("DP4", "Doctor Patel", "Dermatologist", "15 years", "Skin Conditions"))
        self.doctors.append(Doctor("DL5", "Doctor Lee", "Oncologist", "7 years", "Cancer Treatment"))
        self.doctors.append(Doctor("DG6", "Doctor Gupta", "Pediatrician", "9 years", "Child Healthcare"))
        self.doctors.append(Doctor("DK7", "Doctor Kim", "Psychiatrist", "11 years", "Mental Health"))

    #Add patient in system
    def ADD(self, patient):
        self.patients[patient.id_patient] = patient
        print()
        print(patient.name + " with id = " + patient.id_patient + " added successfully")

    #Update patient in the system
    def UPDATE(self, id_patient, new_condition):
        if id_patient in self.patients:
            updated_patient_name = self.patients[id_patient].name  
            self.patients[id_patient].current_condition = new_condition
            print()
            print(updated_patient_name + " condition updated successfully")
        else:
            self.NOT_FOUND_METHOD()

    #Remove patient from the system
    def REMOVE(self, id_patient):
        if id_patient in self.patients:
            removed_patient_name = self.patients.pop(id_patient).name 
            return removed_patient_name
        else:
            return None

    #View the details of patient admitted in the hospital
    def VIEW(self):
        print("=====================================================================================")
        print("|                                   All Patients                                    |")
        print("=====================================================================================")
        print("|   ID    |       Name        | Age | Height | History | Condition | Admission Date |")
        print("=====================================================================================")
        #used loop here to print all patients
        for patient in self.patients.values():
            print()
            print("ID: " + str(patient.id_patient))
            print("Name: " + patient.name)
            print("Age: " + str(patient.age))
            print("Height: " + str(patient.height))
            print("History: " + patient.medical_history)
            print("Condition: " + patient.current_condition)
            print("Admission Date: " + patient.admission_date)
            print()
        print("=====================================================================================")
    
    #View all doctors present in hospital
    def VIEW_D(self):
        print("=====================================================================================")
        print("|                                     All Doctors                                   |")
        print("=====================================================================================")
        print("|   ID   |      Name      |   Specialty   |  Experience  |         Surgeon Of       |")
        print("=====================================================================================")
        #used loop here to print all doctors
        for doctor in self.doctors:
            print()
            print("ID: " + doctor.id_doctor)
            print("Name: " + doctor.name)
            print("Specialty: " + doctor.specialty)
            print("Experience: " + doctor.experience)
            print("Surgeon Of: " + doctor.surgeon_of)
            print()
        print("=====================================================================================")
    
    #schedule the appointment function
    def SCHEDULE(self, patient_id, doctor_id):
        patient = self.patients.get(patient_id)
        if not patient:
            self.NOT_FOUND_METHOD()
            return
        doctor = None
        #used loop here to find doctors
        for doc in self.doctors:
            if doc.id_doctor == doctor_id:
                doctor = doc
                break
        if not doctor:
            print("Doctor Not Found In Hospital")
            return
        print()
        appointment_details = "Appointment for " + patient.name + " scheduled with " + doctor.name + " (" + doctor.specialty + ")"
        doctor_id = str(doctor_id) 
        #put patient and doctor in queue
        if doctor_id not in self.patients_queue:
            self.patients_queue[doctor_id] = deque()
        self.patients_queue[doctor_id].append(appointment_details)
        print("Consultation Appointed")

    #View all appointments of dcotors 
    def VIEW_AP_DR(self):
        print("Appointments of All Doctors:")
        print()
        #used loop here to display all appointments
        for doctor_id, appointments in self.patients_queue.items():
            print("Doctor ID: " + str(doctor_id))
            if appointments:
                for appointment in appointments:
                    print(appointment)
            else:
                print("No appointments scheduled.")
   
    #issue prescription to patient function 
    def ISSUE_PRESCRIPTION(self, doctor_id):
        doctor_exists = False
        #use loop here to find doctors
        for doctor in self.doctors:
            if doctor.id_doctor == doctor_id:
                doctor_exists = True
                break

        if not doctor_exists:
            print("Doctor with ID " + doctor_id + " not found.")
            return

        if doctor_id not in self.patients_queue:
            print("No patients in queue for Doctor " + doctor_id)
            return
        #put appointmnets in the queue
        appointments = self.patients_queue[doctor_id]

        if not appointments:
            print("No patients in queue for Doctor " + doctor_id)
            return
        selected_patient = appointments[0]

        print("Issuing prescription for the first patient in the queue.")
        medication = input("Enter medication: ")
        #Prescription Class calling here to enter details
        prescription = Prescription(selected_patient.split(" ")[2], medication)
        self.prescriptions_stack.append(prescription)
        self.patients_queue[doctor_id].popleft()
        print("Prescription Successful")

    #view prescription entered in the stack
    def VIEW_P(self):
        print("Prescriptions:")
        #used while loop here to traverse stack
        while self.prescriptions_stack:
            prescription = self.prescriptions_stack.pop()
            print()
            print("Patient: " + prescription.patient_name)
            print("Medication: " + prescription.medication)

    #Summary of patients admitted in the hospital
    def SUMMARY_P(self, patient_id):
        patient = self.patients.get(patient_id)
        if patient:
            print("Patient Summary:")
            print("ID: " + patient.id_patient)
            print("Name: " + patient.name)
            print("Age: " + patient.age)
            print("Height: " + patient.height)
            print("Medical History: " + patient.medical_history)
            print("Current Condition: " + patient.current_condition)
            print("Admission Date: " + patient.admission_date)
            print()
            print("Prescription Details:")
            #call prescription class to print prescriptions
            prescriptions = [prescription for prescription in self.prescriptions_stack if prescription.patient_name == patient.name]
            if prescriptions:
                for prescription in prescriptions:
                    print("Medication: " + prescription.medication)
            else:
                print("No prescriptions issued for this patient.")

            # Print doctor appointment details for the patient
            print("\nDoctor Appointment Details:")
            appointment_found = False
            #used loop here to print appointments with doctors present in queue
            for doctor_id, appointments in self.patients_queue.items():
                for appointment in appointments:
                    if patient.name in appointment:
                        print(appointment)
                        appointment_found = True
                        break
            if not appointment_found:
                print("No appointments scheduled for this patient.")
            return

        print("Patient not found.")

    #function used to print patient not found
    def NOT_FOUND_METHOD(self):
        print("Patient Not Found In Hospital")