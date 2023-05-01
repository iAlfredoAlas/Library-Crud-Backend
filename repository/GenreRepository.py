import mysql.connector
from models.genre import Genre
from models.repositoryResponse import RepositoryResponse

#Class of GenreRepository
class GenreRepository:

    #Initialization of the GenreRepository
    def __init__(self, connection):
        self.connection = connection

    def get_all(self, page: int, limit: int):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        
        return RepositoryResponse(result)
    
    def get_all_actives(self, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre WHERE statusGenre = 1 LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        
        return RepositoryResponse(result)
        
    def get_by_id(self, idGenre: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre WHERE idGenre = %s", (idGenre,))
        row = cursor.fetchone()
        if row:
            column_names = [column[0] for column in cursor.description]
            genre_dict = dict(zip(column_names, row))
            return RepositoryResponse(genre_dict)
        else:
            return RepositoryResponse(success=False, error_message="Genre not found")

    def insert(self, genre: Genre):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre WHERE nameGenre = %s", (genre.nameGenre,))

        if cursor.fetchone():
            return RepositoryResponse(success=False, error_message="Genre already exists")
        else:
            try:
                cursor.execute("INSERT INTO genre (nameGenre, statusGenre) VALUES (%s, %s)", (genre.nameGenre,genre.statusGenre))
                self.connection.commit()
                return RepositoryResponse(success=True)
            except mysql.connector.Error as error:
                return RepositoryResponse(success=False, error_message=str(error))

    def update(self, idGenre: int, genre: Genre):
        cursor = self.connection.cursor()
        try:
            # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idGenre FROM genre WHERE nameGenre = %s AND idGenre != %s", (genre.nameGenre, idGenre))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A genre with this name already exists")

            # Actualizar el género
            cursor.execute("UPDATE genre SET nameGenre = %s, statusGenre = %s WHERE idGenre = %s", (genre.nameGenre, genre.statusGenre, idGenre))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="Genre didn't change or genre with id %s not found" % genre.idGenre)
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))

    def delete(self, idGenre: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idGenre FROM genre WHERE idGenre = %s and statusGenre = 0", (idGenre,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A genre with this Id has already been deleted")

            cursor.execute("UPDATE genre SET statusGenre = 0 WHERE idGenre = %s", (idGenre,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Genre with id %s not found" % idGenre)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))

    def activate(self, idGenre: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idGenre FROM genre WHERE idGenre = %s and statusGenre = 1", (idGenre,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A genre with this Id has already been Activate")

            cursor.execute("UPDATE genre SET statusGenre = 1 WHERE idGenre = %s", (idGenre,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Genre with id %s not found" % idGenre)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))
