from Hospital import Hospital
from printmenu import print_menu
from patient import Patient

#main function of code
def main():
    #Class of Hospital 
    hospital = Hospital()

    #used loop here to show menu
    while True:
        print()
        print_menu()

        print()
        choice = input("Enter your choice: ")
        print()
        
        if choice == '1':
            print("Please provide the following information about the patient:")
            id_patient = input("ID: ")
            name_patient = input("Name: ")
            age_patient = input("Age: ")
            height = input("Height: ")
            history = input("Medical Background: ")
            cond = input("Current Condition: ")
            admission_date = input("Admission Date: ")
            #Patient class used here to enter details 
            patient = Patient(id_patient, name_patient, age_patient, history, cond, admission_date, height)
            hospital.ADD(patient)

        elif choice == '2':
            print("Please provide the following information for Updating the patient:")
            id_patient = input("ID = ")
            cond = input("Current Condition = ")
            #update function
            hospital.UPDATE(id_patient, cond)

        elif choice == '3':
            print("Please provide the following information for removal of patient:")
            id_patient = input("Enter patient ID to remove: ")
            #remove function
            removed_patient_name = hospital.REMOVE(id_patient)
            if removed_patient_name:
                print(removed_patient_name + " removed successfully.")
            else:
                hospital.NOT_FOUND_METHOD()

        elif choice == '4':
            #hospital view function
            hospital.VIEW()
        
        elif choice == '5':
            hospital.VIEW_D()
            print()
            hospital.VIEW()
            print()
            print("Please provide the following information to schedule an appointment:")
            print()
            patient_id = input("Patient ID: ")
            doctor_id = input("Doctor ID: ")
            #schedule method of hospital
            hospital.SCHEDULE(patient_id, doctor_id)

        elif choice == '6':
            hospital.VIEW_AP_DR()

        elif choice == '7':
            doctor_id = input("Doctor ID: ")
            #prescription issue function
            hospital.ISSUE_PRESCRIPTION(doctor_id)

        elif choice == '8':
            hospital.VIEW_P()

        elif choice == '9':
            patient_id = input("Enter patient ID: ")
            #summary of patients
            hospital.SUMMARY_P(patient_id)

        elif choice == '10':
            print("Exit")
            break

        else:
            print("Invalid choice. Please try again.")

#call main function
if __name__ == "__main__":
    main()