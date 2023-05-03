#Requerid imports
from services.dbContext import DbContext
from repository.AuthorRepository import AuthorRepository
from models.repositoryResponse import RepositoryResponse
from models.book import Book
from datetime import date

#Class of BookService
class BookService:

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