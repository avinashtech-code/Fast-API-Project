from fastapi import FastAPI , Path
import json 

app = FastAPI() 


def load_data():
    with open('patient.json' , 'r') as f :
        data = json.load(f) 
    return data 
@app.get("/")
def hello() :
    return {'message':'Patient Management System'}

@app.get("/about")
def about():
    return {"message": "This a patient related project"}

@app.get("/view")
def view() :
    data = load_data() 
    return data 

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description = "id of patient",example ="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else :
        return {"error" : "patient not found"}
