import mysql.connector
from models.genre import Genre
from models.repositoryResponse import RepositoryResponse

#Class of GenreRepository
class GenreRepository:

    #Initialization of the GenreRepository
    def __init__(self, connection):
        self.connection = connection


    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre")
        genres = []
        for (idGenre, nameGenre, statusGenre) in cursor:
            genre = Genre(idGenre, nameGenre, statusGenre)
            genres.append(genre)
        return RepositoryResponse(genres)
    
    def get_all_active(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre where statusGenre = 1")
        genres = []
        for (idGenre, nameGenre, statusGenre) in cursor:
            genre = Genre(idGenre, nameGenre, statusGenre)
            genres.append(genre)
        return RepositoryResponse(genres)

    def get_by_id_active(self, idGenre: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre WHERE idGenre = %s and statusGenre = 1", (idGenre,))
        row = cursor.fetchone()
        if row:
            return RepositoryResponse(Genre(*row))
        else:
            return RepositoryResponse(success=False, error_message="Genre not found")
        
    def get_by_id(self, idGenre: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre WHERE idGenre = %s", (idGenre,))
        row = cursor.fetchone()
        if row:
            return RepositoryResponse(Genre(*row))
        else:
            return RepositoryResponse(success=False, error_message="Genre not found")

    def insert(self, genre: Genre):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO genre (nameGenre, statusGenre) VALUES (%s, %s)", (genre.getNameGenre(),genre.getStatusGenre()))
            self.connection.commit()
            return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))

    def update(self, genre: Genre):
        cursor = self.connection.cursor()
        try:
            cursor.execute("UPDATE genre SET nameGenre = %s, statusGenre = %s WHERE idGenre = %s", (genre.getNameGenre(), genre.getStatusGenre(), genre.getIdGenre()))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="Genre with id %s not found" % genre.getIdGenre())
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))


    def delete(self, idGenre: int):
        cursor = self.connection.cursor()
        try:
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
            cursor.execute("UPDATE genre SET statusGenre = 1 WHERE idGenre = %s", (idGenre,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Genre with id %s not found" % idGenre)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))
