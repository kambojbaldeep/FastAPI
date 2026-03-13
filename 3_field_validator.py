from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        
        valid_domains = ["hdfc.com", "icici.com"]

        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Invalid domain name")

        return value

    @field_validator("name")
    @classmethod

    def transform_name(cls, value):
        return value.upper()

        


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted into the database")

patient_info = {"name": "Baldeep","email": "abc@hdfc.com", "age": 30, "weight": 70.5, "married": True, "contact_details": {"phone": "123-456-7890"}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)