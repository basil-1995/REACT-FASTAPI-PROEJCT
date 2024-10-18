from fastapi import FastAPI,Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from .models import Employee
from .config import employee_collection

app = FastAPI()


@app.get("/")
def home():
    return {"home page is loaded"}

@app.post("/add_employee")
def add_employee(employee:Employee):
    employeeobj= employee.dict()

    result = employee_collection.insert_one(employeeobj)
    return result.inserted_id




@app.get("/get_employeelist")
def get_employeelist(employee:Employee):
    employee_list = employee_collection.find()
    return list(employee_list)




