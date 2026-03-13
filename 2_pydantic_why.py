from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(min_length=2, max_length=50, title="Name of the patient", description="Give the name of the patient in less than 50 characters", examples=["Baldeep", "Singh"])]

    email: EmailStr

    linkedin: AnyUrl

    age: int = Field(gt=0, lt=120, description="Age of the patient")

    weight: float = Field(gt=0, lt=200, description="Weight of the patient")

    # married: Optional[bool] = False

    married: Annotated[bool, Field(default=None, description="Whether the patient is married or not")]

    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]

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
