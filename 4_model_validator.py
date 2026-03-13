from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @model_validator(mode="after")
    def energency_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Emergency contact is required for patients above 60")
        return model

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted into the database")

patient_info = {"name": "Baldeep","email": "abc@hdfc.com", "age": 67,"allergies": ["peanuts", "shellfish"], "weight": 70.5, "married": True, "contact_details": {"phone": "123-456-7890", "emergency": "9876543210"}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)