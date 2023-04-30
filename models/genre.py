#Create model to Genre object
class Genre:
    #Initial Genre object
    def __init__(self, idGenre, nameGenre, statusGenre = None):
        self.idGenre = idGenre
        self.nameGenre = nameGenre
        self.statusGenre = statusGenre if statusGenre is not None else True

    #Getters and Setters to Genre
    def getIdGenre(self):
        return self.idGenre

    def getNameGenre(self):
        return self.nameGenre
    
    def getStatusGenre(self):
        return self.statusGenre

    def setIdGenre(self, idGenre):
        self.idGenre = idGenre

    def setNameGenre(self, nameGenre):
        self.nameGenre = nameGenre

    def setStatusGenre(self, statusGenre):
        self.statusGenre = statusGenre
        
    #Methot ToString to Genre
    def __str__(self):
        return f"Genre({self.idGenre}, {self.nameGenre}, {self.statusGenre})"
