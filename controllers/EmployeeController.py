#Requeried imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional

from services.EmployeeService import EmployeeService
from models.repositoryResponse import RepositoryResponse
from models.employee import Employee

#Create route
EmployeeRoute = APIRouter()

#This controller can be uses like this "/Employee?page=2&limit=20"
@EmployeeRoute.get("/Employee", tags=["Employee"], summary="To add pagination use '/Employee?page=1&limit=10&actives=True'")
async def getEmployee(page: Optional[int] = 1, limit: Optional[int] = 10, actives: Optional[bool] = False):

    employeeResult:RepositoryResponse = await EmployeeService.getEmployee(page, limit, actives)
    
    if employeeResult.success:
        return JSONResponse(employeeResult.content)
    else:
        return JSONResponse(employeeResult.error_message, status_code=400)

#Controller to get employee by id    
@EmployeeRoute.get("/Employee/{idEmployee}", tags=["Employee"])
async def getEmployeesById(idEmployee: int):
    
    employeeResult:RepositoryResponse = await EmployeeService.getEmployeeById(idEmployee)
    
    if employeeResult.success:
        return JSONResponse(employeeResult.content)
    else:
        return JSONResponse(employeeResult.error_message, status_code=400)

#Controller to post new Employee    
@EmployeeRoute.post("/Employee", tags=["Employee"])
async def postEmployee(Employee: Employee):
    employeeResult:RepositoryResponse = await EmployeeService.insertEmployee(Employee)
    
    if employeeResult.success:
        return JSONResponse(f"Employee {Employee.nameEmployee} successfully added")
    else:
        return JSONResponse(employeeResult.error_message, status_code=400)

#Controller to edit Employee
@Employee.put("/Employee/{idEmployee}", tags=["Employee"])
async def putEmployee(idEmployee: int, Employee: Employee):
    employeeResult:RepositoryResponse = await EmployeeService.updateEmployee(idEmployee, Employee)
    
    if employeeResult.success:
        return JSONResponse(f"Employee {Employee.nameEmployee} successfully edited")
    else:
        return JSONResponse(employeeResult.error_message, status_code=400)

#Controller to delete Employee    
@EmployeeRoute.delete("/Employee/{idEmployee}", tags=["Employee"])
async def deleteEmployee(idEmployee: int):
    employeeResult:RepositoryResponse = await EmployeeService.deleteEmployee(idEmployee)
    
    if employeeResult.success:
        return JSONResponse(f"Employee with Id {idEmployee} successfully deleted")
    else:
        return JSONResponse(employeeResult.error_message, status_code=400)
    
#Controller to activate AuEmployee    
@EmployeeRoute.put("/Employee/Activate/{idEmployee}", tags=["Employee"])
async def activateEmployee(idEmployee: int):
    employeeResult:RepositoryResponse = await EmployeeService.activeEmployee(idEmployee)
    
    if employeeResult.success:
        return JSONResponse(f"Auhtor with Id {idEmployee} successfully activated")
    else:
        return JSONResponse(employeeResult.error_message, status_code=400)
