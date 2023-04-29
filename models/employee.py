class Employee:
    def __init__(self, idEmployee, nameEmployee, employeeNumber):
        self.idEmployee = idEmployee
        self.nameEmployee = nameEmployee
        self.employeeNumber = employeeNumber

    def getIdEmployee(self):
        return self.idEmployee

    def getNameEmployee(self):
        return self.nameEmployee

    def getEmployeeNumber(self):
        return self.employeeNumber

    def setIdEmployee(self, idEmployee):
        self.idEmployee = idEmployee

    def setNameEmployee(self, nameEmployee):
        self.nameEmployee = nameEmployee

    def setEmployeeNumber(self, employeeNumber):
        self.employeeNumber = employeeNumber

    def __str__(self):
        return f"Employee({self.idEmployee}, {self.nameEmployee}, {self.employeeNumber})"
