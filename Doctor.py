#Doctor class with attributes
class Doctor:
    def __init__(self, id_doctor, name, specialty, experience, surgeon_of):
        self.id_doctor = id_doctor       #doctor id
        self.name = name                 #doctor name
        self.specialty = specialty       #doctor speciality
        self.experience = experience     #doctor experience
        self.surgeon_of = surgeon_of     #surgeon of attribute
