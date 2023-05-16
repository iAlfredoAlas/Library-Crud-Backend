import mysql.connector
from models.book import Book
from models.repositoryResponse import RepositoryResponse

#Class of BookRepository
class BookRepository:
    
    #Initialization of the BookRepository
    def __init__(self, connection):
        self.connection = connection

    def getAll(self, page: int, limit: int):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT b.*, a.*, e.*, g.*, r.* FROM Book b LEFT JOIN Author a ON b.idAuthor = a.idAuthor LEFT JOIN Editorial e ON b.idEditorial = e.idEditorial LEFT JOIN Genre g ON b.idGenre = g.idGenre LEFT JOIN Rack r ON b.idRack = r.idRack LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()

        books = [
            {
                "idBook": book[0],
                "bookName": book[1],
                "publicationDate": str(book[2]),
                "totalPague": book[3],
                "quantityStock": book[4],
                "bookCover": book[5],
                "statusBook": book[6],
                "idAuthor": book[7],
                "Author": {
                    "idAuthor": book[11],
                    "nameAuthor": book[12],
                    "countryBirth": book[13],
                    "dateBorn": str(book[14]),
                    "statusAuthor": book[15]
                },
                "idEditorial": book[8],
                "Editorial": {
                    "idEditorial": book[16],
                    "nameEditorial": book[17],
                    "dateAdd": str(book[18]),
                    "statusEditorial": book[19]
                },
                "idGenre": book[9],
                "Genre": {
                    "idGenre": book[20],
                    "nameGenre": book[21],
                    "statusGenre": book[22],
                },
                "idRack": book[10],
                "Rack": {
                    "idRack": book[23],
                    "nameRack": book[24],
                    "levels": book[25],
                    "statusRack": book[26],
                },
            }
            for book in rows
        ]
        
        return RepositoryResponse(books)
    
    def getAllActives(self, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT b.*, a.*, e.*, g.*, r.* FROM Book b LEFT JOIN Author a ON b.idAuthor = a.idAuthor LEFT JOIN Editorial e ON b.idEditorial = e.idEditorial LEFT JOIN Genre g ON b.idGenre = g.idGenre LEFT JOIN Rack r ON b.idRack = r.idRack where statusBook = 1 LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()

        books = [
            {
                "idBook": book[0],
                "bookName": book[1],
                "publicationDate": str(book[2]),
                "totalPague": book[3],
                "quantityStock": book[4],
                "bookCover": book[5],
                "statusBook": book[6],
                "idAuthor": book[7],
                "Author": {
                    "idAuthor": book[11],
                    "nameAuthor": book[12],
                    "countryBirth": book[13],
                    "dateBorn": str(book[14]),
                    "statusAuthor": book[15]
                },
                "idEditorial": book[8],
                "Editorial": {
                    "idEditorial": book[16],
                    "nameEditorial": book[17],
                    "dateAdd": str(book[18]),
                    "statusEditorial": book[19]
                },
                "idGenre": book[9],
                "Genre": {
                    "idGenre": book[20],
                    "nameGenre": book[21],
                    "statusGenre": book[22],
                },
                "idRack": book[10],
                "Rack": {
                    "idRack": book[23],
                    "nameRack": book[24],
                    "levels": book[25],
                    "statusRack": book[26],
                },
            }
            for book in rows
        ]
        
        return RepositoryResponse(books)
    
    def getById(self, idBook: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT b.*, a.*, e.*, g.*, r.* FROM Book b LEFT JOIN Author a ON b.idAuthor = a.idAuthor LEFT JOIN Editorial e ON b.idEditorial = e.idEditorial LEFT JOIN Genre g ON b.idGenre = g.idGenre LEFT JOIN Rack r ON b.idRack = r.idRack where idBook = %s", (idBook,))
        row = cursor.fetchone()
        if row:
            books = [
            {
                "idBook": row[0],
                "bookName": row[1],
                "publicationDate": str(row[2]),
                "totalPague": row[3],
                "quantityStock": row[4],
                "bookCover": row[5],
                "statusBook": row[6],
                "idAuthor": row[7],
                "Author": {
                    "idAuthor": row[11],
                    "nameAuthor": row[12],
                    "countryBirth": row[13],
                    "dateBorn": str(row[14]),
                    "statusAuthor": row[15]
                },
                "idEditorial": row[8],
                "Editorial": {
                    "idEditorial": row[16],
                    "nameEditorial": row[17],
                    "dateAdd": str(row[18]),
                    "statusEditorial": row[19]
                },
                "idGenre": row[9],
                "Genre": {
                    "idGenre": row[20],
                    "nameGenre": row[21],
                    "statusGenre": row[22],
                },
                "idRack": row[10],
                "Rack": {
                    "idRack": row[23],
                    "nameRack": row[24],
                    "levels": row[25],
                    "statusRack": row[26],
                },
            }
        ]
            return RepositoryResponse(books)
        else:
            return RepositoryResponse(success=False, error_message="Book not found")
        

        #Method insert Book
    def insert(self, book: Book):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Book WHERE bookName = %s", (book.bookName,))

        if cursor.fetchone():
            return RepositoryResponse(success=False, error_message="Book already exists")
        else:
            try:
                cursor.execute("INSERT INTO Book (bookName, publicationDate, totalPague, quantityStock, bookCover, statusBook, idAuthor, idEditorial, idGenre, idRack) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (book.bookName, book.publicationDate, book.totalPague, book.quantityStock, book.bookCover, book.statusBook, book.idAuthor, book.idEditorial, book.idGenre, book.idRack))
                self.connection.commit()
                return RepositoryResponse(success=True)
            except mysql.connector.Error as error:
                return RepositoryResponse(success=False, error_message="Can not insert Book, %s" % str(error))
    
    #Method update Authrs
    def update(self, idBook: int, book: Book):
        cursor = self.connection.cursor()
        try:
            # Verificar si existe un autor con el mismo nombre
            cursor.execute("SELECT * FROM Book WHERE bookName = %s AND idBook != %s", (book.bookName, idBook))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A book with this name already exists")

            # Actualizar el book
            cursor.execute("UPDATE Book SET bookName = %s, publicationDate = %s, totalPague = %s, quantityStock = %s, bookCover = %s, statusBook = %s, idAuthor = %s, idEditorial = %s, idGenre = %s, idRack = %s WHERE idBook = %s", (book.bookName, book.publicationDate, book.totalPague, book.quantityStock, book.bookCover, book.statusBook, book.idAuthor, book.idEditorial, book.idGenre, book.idRack, idBook))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="Book didn't change or book with id %s not found" % idBook)
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not updtae Book, %s" % str(error))
        

    #Method delete AutBookhor   
    def delete(self, idBook: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un book con ese idbook
            cursor.execute("SELECT * FROM Book WHERE bookName = %s and statusBook = 0", (idBook,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A book with this Id has already been deleted")

            cursor.execute("UPDATE Book SET statusBook = 0 WHERE idBook = %s", (idBook,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Book with id %s not found" % idBook)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not delete Book, %s" % str(error))


    #Method activate Book
    def activate(self, idBook: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un Book con ese idBook
            cursor.execute("SELECT * FROM Book WHERE bookName = %s and statusBook = 1", (idBook,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A book with this Id has already been activate")

            cursor.execute("UPDATE Book SET statusBook = 1 WHERE idBook = %s", (idBook,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Book with id %s not found" % idBook)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not activate Book, %s" % str(error))


    