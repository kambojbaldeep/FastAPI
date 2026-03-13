from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address


address_dict = {"city": "Gurgaon", "state": "Haryana", "zip_code": "122001"}

address_1 = Address(**address_dict)

patient_dict = {"name": "Baldeep", "age": 30, "gender": "male", "address": address_1}

patient_1 = Patient(**patient_dict)

print(patient_1)
print(patient_1.name)
print(patient_1.address.city)
print(patient_1.address.state)
print(patient_1.address.zip_code)