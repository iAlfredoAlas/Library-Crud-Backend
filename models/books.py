class Books:
    def __init__(self, idBook, bookName, publicationDate, totalPage, quantityStock, idAutor, idEditorial, idGenre, idRack):
        self.idBook = idBook
        self.bookName = bookName
        self.publicationDate = publicationDate
        self.totalPage = totalPage
        self.quantityStock = quantityStock
        self.idAutor = idAutor
        self.idEditorial = idEditorial
        self.idGenre = idGenre
        self.idRack = idRack

    def getIdBook(self):
        return self.idBook

    def getBookName(self):
        return self.bookName

    def getPublicationDate(self):
        return self.publicationDate

    def getTotalPage(self):
        return self.totalPage

    def getQuantityStock(self):
        return self.quantityStock

    def getIdAutor(self):
        return self.idAutor

    def getIdEditorial(self):
        return self.idEditorial

    def getIdGenre(self):
        return self.idGenre

    def getIdRack(self):
        return self.idRack

    def setIdBook(self, idBook):
        self.idBook = idBook

    def setBookName(self, bookName):
        self.bookName = bookName

    def setPublicationDate(self, publicationDate):
        self.publicationDate = publicationDate

    def setTotalPage(self, totalPage):
        self.totalPage = totalPage

    def setQuantityStock(self, quantityStock):
        self.quantityStock = quantityStock

    def setIdAutor(self, idAutor):
        self.idAutor = idAutor

    def setIdEditorial(self, idEditorial):
        self.idEditorial = idEditorial

    def setIdGenre(self, idGenre):
        self.idGenre = idGenre

    def setIdRack(self, idRack):
        self.idRack = idRack

    def __str__(self):
        return f"Libros({self.idBook}, {self.bookName}, {self.publicationDate}, {self.totalPage}, {self.quantityStock}, {self.idAutor}, {self.idEditorial}, {self.idGenre}, {self.idRack})"
