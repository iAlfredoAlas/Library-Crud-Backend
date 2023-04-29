class User:
    def __init__(self, idUser, nameUser, carnetUser, emailUser, phoneUser):
        self.idUser = idUser
        self.nameUser = nameUser
        self.carnetUser = carnetUser
        self.emailUser = emailUser
        self.phoneUser = phoneUser

    def getIdUser(self):
        return self.idUser

    def getNameUser(self):
        return self.nameUser

    def getCarnetUser(self):
        return self.carnetUser

    def getEmailUser(self):
        return self.emailUser

    def getPhoneUser(self):
        return self.phoneUser

    def setIdUser(self, idUser):
        self.idUser = idUser

    def setNameUser(self, nameUser):
        self.nameUser = nameUser

    def setCarnetUser(self, carnetUser):
        self.carnetUser = carnetUser

    def setEmailUser(self, emailUser):
        self.emailUser = emailUser

    def setPhoneUser(self, phoneUser):
        self.phoneUser = phoneUser

    def __str__(self):
        return f"User({self.idUser}, {self.nameUser}, {self.carnetUser}, {self.emailUser}, {self.phoneUser})"
