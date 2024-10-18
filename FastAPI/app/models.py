from pydantic import BaseModel

class Designation(BaseModel):
    DesignationName :str


class Department(BaseModel):
    DepartmentName : str

class EmployeeType(BaseModel):
    EmployeeTypeName:str

class Status(BaseModel):
    StatusName :str

class Employee(BaseModel):
    FirstName:str
    LastName:str
    JoinedOn:str
    Age:int
    Designation:Designation
    Department:Department
    EmployeeType:EmployeeType
    Status:Status