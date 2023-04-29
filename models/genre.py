class Genre:
    def __init__(self, idGenre, nameGenre):
        self.idGenre = idGenre
        self.nameGenre = nameGenre

    def getId(self):
        return self.idGenre

    def getName(self):
        return self.nameGenre

    def setId(self, idGenre):
        self.idGenre = idGenre

    def setName(self, nameGenre):
        self.nameGenre = nameGenre

    def __str__(self):
        return f"Genre({self.idGenre}, {self.nameGenre})"
