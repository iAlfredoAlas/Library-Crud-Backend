#Requerid imports
from services.dbContext import DbContext
from repository.BookRepository import BookRepository
from models.repositoryResponse import RepositoryResponse
from models.book import Book
from datetime import date

#Class of BookService
class BookService:

    #Pagination to Book
    async def getBook(page: int, limit: int, actives: bool):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = BookRepository(dbConnection.connection).getAll(page, limit) if not actives else BookRepository(dbConnection.connection).getAllActives(page, limit)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    #Get Book by id    
    async def getBookById(idBook: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = BookRepository(dbConnection.connection).getById(idBook)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")