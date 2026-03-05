def insert_patient_data(name: str, age: int):

    if type(name) == str and type(age) ==  int:
        print(name)
        print(age)
        print("inserted into the database")
    else:
        print("Invalid data types")

insert_patient_data("Baldeep", "thirty")