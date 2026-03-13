from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float  #kg
    height: float  #meters
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height * self.height), 2)
        return bmi


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI: ", patient.calculate_bmi)
    print("inserted into the database")

patient_info = {"name": "Baldeep","email": "abc@hdfc.com", "age": 67,"allergies": ["peanuts", "shellfish"], "weight": 170.5, "height": 1.75, "married": True, "contact_details": {"phone": "123-456-7890", "emergency": "9876543210"}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)