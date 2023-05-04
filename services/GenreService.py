from services.dbContext import DbContext
from repository.GenreRepository import GenreRepository
from models.repositoryResponse import RepositoryResponse
from models.genre import Genre

#Class of GenreRepository
class GenreService:

    async def get_genres(page: int, limit: int, actives: bool):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = GenreRepository(dbConnection.connection).get_all(page, limit) if not actives else GenreRepository(dbConnection.connection).get_all_actives(page, limit)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def get_genre_by_id(idGenre: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = GenreRepository(dbConnection.connection).get_by_id(idGenre)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def insert_genre(Genre: Genre):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el genero es correcto
            if not Genre.nameGenre.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")

            repo_response: RepositoryResponse = GenreRepository(dbConnection.connection).insert(Genre)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def update_genre(idGenre: int, Genre: Genre):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el genero es correcto
            if not Genre.nameGenre.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")

            repo_response: RepositoryResponse = GenreRepository(dbConnection.connection).update(idGenre, Genre)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def delete_genre(idGenre: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = GenreRepository(dbConnection.connection).delete(idGenre)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def Activate_genre(idGenre: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = GenreRepository(dbConnection.connection).activate(idGenre)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        

