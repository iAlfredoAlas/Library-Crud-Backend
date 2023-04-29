class Reserve:
    def __init__(self, idReservation, idBook, idEmployee, idUser):
        self.idReservation = idReservation
        self.idBook = idBook
        self.idEmployee = idEmployee
        self.idUser = idUser

    def getIdReservation(self):
        return self.idReservation

    def getIdBook(self):
        return self.idBook

    def getIdEmployee(self):
        return self.idEmployee

    def getIdUser(self):
        return self.idUser

    def setIdReservation(self, idReservation):
        self.idReservation = idReservation

    def setIdBook(self, idBook):
        self.idBook = idBook

    def setIdEmployee(self, idEmployee):
        self.idEmployee = idEmployee

    def setIdUser(self, idUser):
        self.idUser = idUser

    def __str__(self):
        return f"Reserve({self.idReservation}, {self.idBook}, {self.idEmployee}, {self.idUser})"
