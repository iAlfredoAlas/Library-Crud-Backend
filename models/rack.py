class Rack:
    def __init__(self, idRack, nameRack):
        self.idRack = idRack
        self.nameRack = nameRack

    def getId(self):
        return self.idRack

    def getName(self):
        return self.nameRack

    def setId(self, idRack):
        self.idRack = idRack

    def setName(self, nameRack):
        self.nameRack = nameRack

    def __str__(self):
        return f"Rack({self.idRack}, {self.nameRack})"
