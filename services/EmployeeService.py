#Requerid imports
from services.dbContext import DbContext
from repository.EmployeeRepository import EmployeeRepository
from models.repositoryResponse import RepositoryResponse
from models.employee import Employee

#Class of EmployeeService
class EmployeeService:

    #Pagination to Employee
    async def getEmployee(page: int, limit: int, actives: bool):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = EmployeeRepository(dbConnection.connection).getAll(page, limit) if not actives else EmployeeRepository(dbConnection.connection).getAllActives(page, limit)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    #Get Employee by id    
    async def getEmployeeById(idEmployee: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = EmployeeRepository(dbConnection.connection).getById(idEmployee)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

   
    #Insert Employees    
    async def insertEmployee(Employee: Employee):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el autor es correcto
            if not Employee.nameEmployee.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")
            
        
             # Validar si el numero de empleados no es vacio
            if not Employee.employeeNumber.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un dato valido")

            repo_response: RepositoryResponse = EmployeeRepository(dbConnection.connection).insert(Employee)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Update Employees    
    async def updateEmployee(idEmployee: int, Employee: Employee):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el autor es correcto
            if not Employee.nameEmployee.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")
            
             # Validar si el numero de empleados no es vacio
            if not Employee.employeeNumber.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un dato valido")

            repo_response: RepositoryResponse = EmployeeRepository(dbConnection.connection).update(idEmployee, Employee)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Delete Employee    
    async def deleteEmployee(idEmployee: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = EmployeeRepository(dbConnection.connection).delete(idEmployee)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Active Employee    
    async def activeEmployee(idEmployee: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = EmployeeRepository(dbConnection.connection).activate(idEmployee)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
   