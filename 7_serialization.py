from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str = "male"
    address: Address


address_dict = {"city": "Gurgaon", "state": "Haryana", "zip_code": "122001"}

address_1 = Address(**address_dict)

patient_dict = {"name": "Baldeep", "age": 30, "gender": "male", "address": address_1}

patient_1 = Patient(**patient_dict)


temp = patient_1.model_dump()
print(temp)
print(type(temp))


temp_json = patient_1.model_dump_json()
print(temp_json)
print(type(temp_json))


temp_name = patient_1.model_dump_json(include=["name"])
print(temp_name)
print(type(temp_name))


temp_exclude = patient_1.model_dump_json(exclude=["name"])
print(temp_exclude)
print(type(temp_exclude))


temp_exclude_state = patient_1.model_dump_json(exclude={"address": ["state"]})
print(temp_exclude_state)
print(type(temp_exclude_state))


patient_dict_2 = {"name": "Baldeep", "age": 30, "address": address_1}

patient_2 = Patient(**patient_dict_2)

print(patient_2)

temp_exclude_unset = patient_2.model_dump_json(exclude_unset=True)
print(temp_exclude_unset)
print(type(temp_exclude_unset))