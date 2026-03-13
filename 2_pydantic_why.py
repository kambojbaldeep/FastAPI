from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    email: EmailStr
    linkedin: AnyUrl
    age: int
    weight: float
    married: Optional[bool] = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]



def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted into the database")

patient_info = {"name": "Baldeep","email": "abc@gmail.com", "linkedin": "https://www.linkedin.com/in/baldeep-singh-kamboj/", "age": 30, "weight": 70.5, "married": True, "contact_details": {"phone": "123-456-7890"}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
