def insert_patient_data(name: str, age: int):

    if type(name) == str and type(age) ==  int:
        print(name)
        print(age)
        print("inserted into the database")
    else:
        raise TypeError("Incorrect data type")

insert_patient_data("Baldeep", 30)