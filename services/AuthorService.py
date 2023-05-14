#Requerid imports
from services.dbContext import DbContext
from repository.AuthorRepository import AuthorRepository
from models.repositoryResponse import RepositoryResponse
from models.author import Author
from datetime import date

#Class of AuthorService
class AuthorService:

    #Pagination to Author
    async def getAuthor(page: int, limit: int, actives: bool):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = AuthorRepository(dbConnection.connection).getAll(page, limit) if not actives else AuthorRepository(dbConnection.connection).getAllActives(page, limit)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    #Get Author by id    
    async def getAuthorById(idAuthor: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = AuthorRepository(dbConnection.connection).getById(idAuthor)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Insert Authors    
    async def insertAuthor(Author: Author):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el autor es correcto
            if not Author.nameAuthor.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")
            if Author.dateBorn <= date(1700, 1, 1):
                return RepositoryResponse(success=False, error_message=f"La fecha es incorrecta o es minima {Author.dateBorn}")
            if Author.dateBorn != date('%Y,%m,%d'):
                return RepositoryResponse(success=False, error_message=f"El formato de fecha es diferente de 'yyyy,mm,dd' ")
            repo_response: RepositoryResponse = AuthorRepository(dbConnection.connection).insert(Author)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Update Authors    
    async def updateAuthor(idAuthor: int, Author: Author):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el autor es correcto
            if not Author.nameAuthor.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")
            if Author.dateBorn <= date(1700, 1, 1):
                return RepositoryResponse(success=False, error_message=f"La fecha es incorrecta o es minima {Author.dateBorn}")
            if Author.dateBorn != date('%Y,%m,%d'):
                return RepositoryResponse(success=False, error_message=f"El formato de fecha es diferente de 'yyyy,mm,dd' ")
            repo_response: RepositoryResponse = AuthorRepository(dbConnection.connection).update(idAuthor, Author)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Delete Author    
    async def deleteAuthor(idAuthor: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = AuthorRepository(dbConnection.connection).delete(idAuthor)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Active Author    
    async def activeAuthor(idAuthor: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = AuthorRepository(dbConnection.connection).activate(idAuthor)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
   