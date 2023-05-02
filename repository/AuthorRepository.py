#Requerid imports
import mysql.connector
from models.author import Author
from models.repositoryResponse import RepositoryResponse

#Class of AuthorRepository
class AuthorRepository:

    #initialization of the AuthorRepository
    def __init__(self, connection):
        self.connection = connection
    
    #Method getAll Authors
    def getAll(self, page: int, limit: int):
        offset = (page -1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM author LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        authors = [
            {
                "idAuthor": author[0],
                "nameAuhtor": author[1],
                "countryBirth": author[2],
                "dateBorn": str(author[3]),
                "statusAuthor": author[4]
            }
            for author in rows
        ]

        return RepositoryResponse(authors)
    
    #Method getAllActives
    def getAllActives(self, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM author WHERE statusAuthor = 1 LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        authors = [
            {
                "idAuthor": author[0],
                "nameAuhtor": author[1],
                "countryBirth": author[2],
                "dateBorn": str(author[3]),
                "statusAuthor": author[4]
            }
            for author in rows
        ]
        
        return RepositoryResponse(authors)
    
    #Method getById Authors
    def getById(self, idAuthor: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM author WHERE idAuthor = %s", (idAuthor,))
        row = cursor.fetchone()
        if row:
            authors = [
            {
                "idAuthor": row[0],
                "nameAuthor": row[1],
                "countryBirth": row[2],
                "dateBorn": str(row[3]),
                "statusAuthor": row[4]
            }
        ]
            return RepositoryResponse(authors)
        else:
            return RepositoryResponse(success=False, error_message="Author not found")
        
    #Method insert Authors
    def insert(self, author: Author):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM author WHERE nameAuthor = %s", (author.nameAuthor,))

        if cursor.fetchone():
            return RepositoryResponse(success=False, error_message="Author already exists")
        else:
            try:
                cursor.execute("INSERT INTO author (nameAuthor, countryBirth, dateBorn) VALUES (%s, %s, %s)", (author.nameAuthor, author.countryBirth, author.dateBorn))
                self.connection.commit()
                return RepositoryResponse(success=True)
            except mysql.connector.Error as error:
                return RepositoryResponse(success=False, error_message="Can not insert Author, %s" % str(error))
    
    #Method update Authrs
    def update(self, idAuthor: int, author: Author):
        cursor = self.connection.cursor()
        try:
            # Verificar si existe un autor con el mismo nombre
            cursor.execute("SELECT idAuthor FROM author WHERE nameAuthor = %s AND idAuthor != %s", (author.nameAuthor, idAuthor))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A author with this name already exists")

            # Actualizar el género
            cursor.execute("UPDATE author SET nameAuthor = %s, statusAuthor = %s WHERE idAuthor = %s", (author.nameAuthor, author.statusAuthor, idAuthor))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="Author didn't change or author with id %s not found" % author.idAuthor)
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not updtae Author, %s" % str(error))
        

    #Method delete Author   
    def delete(self, idAuthor: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un author con ese idAuthor
            cursor.execute("SELECT idAuthor FROM author WHERE idAuthor = %s and statusAuthor = 0", (idAuthor,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A author with this Id has already been deleted")

            cursor.execute("UPDATE author SET statusAuthor = 0 WHERE idAuthor = %s", (idAuthor,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Auhtor with id %s not found" % idAuthor)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not delete Author, %s" % str(error))


    #Method activate Author
    def activate(self, idAuthor: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un author con ese idAuthor
            cursor.execute("SELECT idAuthor FROM author WHERE idAuthor = %s and statusAuthor = 1", (idAuthor,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A author with this Id has already been Activate")

            cursor.execute("UPDATE author SET statusAuthor = 1 WHERE idAuthor = %s", (idAuthor,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Author with id %s not found" % idAuthor)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not activate Author, %s" % str(error))
