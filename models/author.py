class Author:
    def __init__(self, idAutor, nameAutor, countryBirth, dateBorn):
        self.idAutor = idAutor
        self.nameAutor = nameAutor
        self.countryBirth = countryBirth
        self.dateBorn = dateBorn

    def getId(self):
        return self.idAutor

    def getName(self):
        return self.nameAutor

    def getCountry(self):
        return self.countryBirth

    def getDateBorn(self):
        return self.dateBorn

    def setId(self, idAutor):
        self.idAutor = idAutor

    def setName(self, nameAutor):
        self.nameAutor = nameAutor

    def setCountry(self, countryBirth):
        self.countryBirth = countryBirth

    def setDateBorn(self, dateBorn):
        self.dateBorn = dateBorn

    def __str__(self):
        return f"Autor({self.idAutor}, {self.nameAutor}, {self.countryBirth}, {self.dateBorn})"
