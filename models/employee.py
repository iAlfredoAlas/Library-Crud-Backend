#Requeried imports
from pydantic import BaseModel
from typing import Optional

#Create model to Employee object
class Employee(BaseModel):
   
    idEmployee: int = 0
    nameEmployee: str = ""
    employeeNumber: str = ""
    statusEmployee: bool = True

