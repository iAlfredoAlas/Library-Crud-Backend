import mysql.connector
from models.genre import Genre
from models.repositoryResponse import RepositoryResponse

class GenreRepository:
    def __init__(self, connection):
        self.connection = connection

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre")
        genres = []
        for (idGenre, nameGenre) in cursor:
            genre = Genre(idGenre, nameGenre)
            genres.append(genre)
        return RepositoryResponse(genres)

    def get_by_id(self, idGenre):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre WHERE idGenre = %s", (idGenre,))
        row = cursor.fetchone()
        if row:
            return RepositoryResponse(Genre(*row))
        else:
            return RepositoryResponse(success=False, error_message="Genre not found")

    def insert(self, genre):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO genre (nameGenre) VALUES (%s)", (genre.getName(),))
            self.connection.commit()
            return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))

    def update(self, genre):
        cursor = self.connection.cursor()
        try:
            cursor.execute("UPDATE genre SET nameGenre = %s WHERE idGenre = %s", (genre.getName(), genre.getId()))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="Genre with id %s not found" % genre.getId())
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))


    def delete(self, idGenre):
        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM genre WHERE idGenre = %s", (idGenre,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="ID not found")
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message=str(error))

