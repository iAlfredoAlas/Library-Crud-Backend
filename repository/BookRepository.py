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
        cursor.execute("SELECT * FROM Book LIMIT %s OFFSET %s", (limit, offset))

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
                "idEditorial": book[8],
                "idGenre": book[9],
                "idRack": book[10],
            }
            for book in rows
        ]
        
        return RepositoryResponse(books)
    
    def getAllActives(self, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Book WHERE statusBook = 1 LIMIT %s OFFSET %s", (limit, offset))

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
                "idEditorial": book[8],
                "idGenre": book[9],
                "idRack": book[10],
            }
            for book in rows
        ]
        
        return RepositoryResponse(books)
    
    def getById(self, idEditorial: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Editorial WHERE idEditorial = %s", (idEditorial,))
        row = cursor.fetchone()
        if row:
            editorials = {
                    "idEditorial": row[0],
                    "nameEditorial": row[1],
                    "dateAdd": str(row[2]),
                    "statusEditorial": row[3]
                }
            return RepositoryResponse(editorials)
        else:
            return RepositoryResponse(success=False, error_message="Editorial not found")

    def insert(self, editorial: Editorial):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Editorial WHERE nameEditorial = %s", (editorial.nameEditorial,))

        if cursor.fetchone():
            return RepositoryResponse(success=False, error_message="Editorial already exists")
        else:
            try:
                cursor.execute("INSERT INTO Editorial (nameEditorial, dateAdd, statusEditorial) VALUES (%s, %s, %s)", (editorial.nameEditorial, editorial.dateAdd, editorial.statusEditorial))
                self.connection.commit()
                return RepositoryResponse(success=True)
            except mysql.connector.Error as error:
                return RepositoryResponse(success=False, error_message="Can not insert editorial, %s" % str(error))

    def update(self, idEditorial: int, editorial: Editorial):
        cursor = self.connection.cursor()
        try:
            # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idEditorial FROM Editorial WHERE nameEditorial = %s AND idEditorial != %s", (editorial.nameEditorial, idEditorial))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="An Editorial with this name already exists")

            # Actualizar el género
            cursor.execute("UPDATE Editorial SET nameEditorial = %s, dateAdd = %s, statusEditorial = %s WHERE idEditorial = %s", (editorial.nameEditorial, editorial.dateAdd, editorial.statusEditorial, idEditorial))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="Editorial didn't change or editorial with id %s not found" % editorial.idEditorial)
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not update editorial, %s" % str(error))

    def delete(self, idEditorial: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idEditorial FROM Editorial WHERE idEditorial = %s and statusEditorial = 0", (idEditorial,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="An editorial with this Id has already been deleted")

            cursor.execute("UPDATE Editorial SET statusEditorial = 0 WHERE idEditorial = %s", (idEditorial,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Editorial with id %s not found" % idEditorial)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not Delete editorial, %s" % str(error))

    def activate(self, idEditorial: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idEditorial FROM Editorial WHERE idEditorial = %s and statusEditorial = 1", (idEditorial,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A editorial with this Id has already been Activate")

            cursor.execute("UPDATE Editorial SET statusEditorial = 1 WHERE idEditorial = %s", (idEditorial,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Editorial with id %s not found" % idEditorial)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not Active editorial, %s" % str(error))