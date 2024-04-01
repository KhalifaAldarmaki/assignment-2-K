#Patient class contains attributes
class Patient:
    def __init__(self, id_patient, name, age, medical_history, current_condition, admission_date, height):
        self.id_patient = id_patient     #patient ID
        self.name = name                 #patient name
        self.age = age                   #pateint age
        self.medical_history = medical_history    #patient medical history
        self.current_condition = current_condition     #patient medical condition 
        self.admission_date = admission_date           #patient admission date in hospital
        self.height = height                           #patient height
