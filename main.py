from fastapi import FastAPI, Path, HTTPException, Query
import json
from pydantic import BaseModel, computed_field, Field
from typing import Annotated, Literal, Optional
from fastapi.responses import JSONResponse

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(...,description="ID of the patient", example="P001")]
    name: Annotated[str, Field(...,description="Name of the patient", example="Baldeep")]
    city: Annotated[str, Field(...,description="City of the patient", example="Gurgaon")]
    age: Annotated[int, Field(...,gt=10, lt=120, description="Age of the patient", example=30)]
    gender: Annotated[Literal["male", "female", "others"], Field(..., description="Gender of the patient", example="male")]
    height: Annotated[float, Field(...,gt=0, description="Height of the patient in meters", example=1.3)]
    weight: Annotated[float, Field(...,gt=0, description="Weight of the patient in kilograms", example=70.5)]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height * self.height), 2)

    @computed_field
    @property
    def bmi_category(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

    
class PatientUpdate(BaseModel):

    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal["male", "female"]], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data

def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f)


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return{"message" : "A fully functional API to manage patient records"}

@app.get("/view")

def view():

    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")):

    # load all patients

    data = load_data()

    if patient_id in data:
        return data[patient_id]

    # else:
    #     return {"error": "Patient not found"}

    raise HTTPException(status_code=404, detail="Patient not found")


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight or BMI"), order: str = Query("asc", description="Sort in Ascending or Descending order") ):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field selected from the {valid_fields}")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order selected between 'asc' or 'desc'")

    data = load_data()

    sort_order = True if order == "desc" else False
    
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    
    return sorted_data


@app.post("/create")

def create_patient(patient: Patient):
    
    #load the existing data
    data = load_data()

    #check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    #new patient add to the database
    data[patient.id] = patient.model_dump(exclude=["id"])

    #save into json file
    save_data(data)

    return JSONResponse(content={"message": "Patient created successfully"}, status_code=201)



@app.put("/edit/{patient_id}")

def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object - > updated bmi + verdict
    existing_patient_info["id"] = patient_id
    patient_pydantic_object = Patient(**existing_patient_info)

    # pydantic object -> dict
    existing_patient_info = patient_pydantic_object.model_dump(exclude=["id"])

    #add tjis dict to data
    data[patient_id] = existing_patient_info

    # save into json file
    save_data(data)

    return JSONResponse(content={"message": "Patient updated successfully"}, status_code=200)

    
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    del data[patient_id]
    save_data(data)
    return JSONResponse(content={"message": "Patient deleted successfully"}, status_code=200)