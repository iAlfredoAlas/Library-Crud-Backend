#Requerid imports
import mysql.connector
from models.employee import Employee
from models.repositoryResponse import RepositoryResponse

##Class of EmployeeRepository
class EmployeeRepository:

    #initialization of the EmployeeRepository
    def __init__(self, connection):
        self.connection = connection
    
    #Method getAll Employees
    def getAll(self, page: int, limit: int):
        offset = (page -1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM employee LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        employees = [
            {
                "idEmployee": employee[0],
                "nameEmployee": employee[1],
                "employeeNumber": employee[2],
                "statusEmployee": employee[3]
            }
            for employee in rows
        ]

        return RepositoryResponse(employees)
    
    #Method getAllActives
    def getAllActives(self, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM employee WHERE statusEmployee = 1 LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        employees = [
            {
                "idEmployee": employee[0],
                "nameEmployee": employee[1],
                "employeeNumber": employee[2],
                "statusEmployee": employee[3]
            }
            for employee in rows
        ]
        
        return RepositoryResponse(employees)
    
    #Method getById Employees
    def getById(self, idEmployee: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM employee WHERE idEmployee = %s", (idEmployee,))
        row = cursor.fetchone()
        if row:
            employees = [
            {
                "idEmployee": row[0],
                "nameEmployee": row[1],
                "employeeNumber": row[2],
                "statusEmployee": row[3]
            }
        ]
            return RepositoryResponse(employees)
        else:
            return RepositoryResponse(success=False, error_message="Employee not found")
        
    #Method insert Employees
    def insert(self, employee: Employee):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM employee WHERE nameEmployee = %s", (employee.nameEmployee,))

        if cursor.fetchone():
            return RepositoryResponse(success=False, error_message="Employee already exists")
        else:
            try:
                cursor.execute("INSERT INTO employee (nameEmployee, employeeNumber) VALUES (%s, %s)", (employee.nameEmployee, employee.employeeNumber))
                self.connection.commit()
                return RepositoryResponse(success=True)
            except mysql.connector.Error as error:
                return RepositoryResponse(success=False, error_message=str(error))
    
    #Method update Employees
    def update(self, idEmployee: int, employee: Employee):
        cursor = self.connection.cursor()
        try:
            # Verificar si existe un Employee con el mismo nombre
            cursor.execute("SELECT idEmployee FROM employee WHERE nameEmployee = %s AND idEmployee != %s", (employee.nameEmployee, idEmployee))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A employee with this name already exists")

            # Actualizar el Employee
            cursor.execute("UPDATE employee SET nameEmployee = %s, statusEmployee = %s WHERE idEmployee = %s", (employee.nameEmployee, employee.statusEmployee, idEmployee))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="Employee didn't change or employee with id %s not found" % employee.idEmployee)
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))
        

    #Method delete Employee   
    def delete(self, idEmployee: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un employee con ese idEmployee
            cursor.execute("SELECT idEmployee FROM employee WHERE idEmployee = %s and statusEmployee = 0", (idEmployee,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A employee with this Id has already been deleted")

            cursor.execute("UPDATE employee SET statusEmployee = 0 WHERE idEmployee = %s", (idEmployee,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Employee with id %s not found" % idEmployee)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))


    #Method activate Employee
    def activate(self, idEmployee: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un employee con ese idEmployee
            cursor.execute("SELECT idEmployee FROM employee WHERE idEmployee = %s and statusEmployee = 1", (idEmployee,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A employee with this Id has already been Activate")

            cursor.execute("UPDATE employee SET statusEmployee = 1 WHERE idEmployee = %s", (idEmployee,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Employee with id %s not found" % idEmployee)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))
