class Editorial:
    def __init__(self, idEditorial, nameEditorial, dateAdd):
        self.idEditorial = idEditorial
        self.nameEditorial = nameEditorial
        self.dateAdd = dateAdd

    def getId(self):
        return self.idEditorial

    def getName(self):
        return self.nameEditorial

    def getDateAdd(self):
        return self.dateAdd

    def setId(self, idEditorial):
        self.idEditorial = idEditorial

    def setName(self, nameEditorial):
        self.nameEditorial = nameEditorial

    def setDateAdd(self, dateAdd):
        self.dateAdd = dateAdd

    def __str__(self):
        return f"Editorial({self.idEditorial}, {self.nameEditorial}, {self.dateAdd})"
