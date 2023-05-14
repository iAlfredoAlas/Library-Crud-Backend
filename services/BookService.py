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
        
        #Insert Books    
    async def insertBook(Book: Book):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el book es correcto
            if not Book.bookName.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")
            
              # Validar si la fecha de publicacion no este vacia 
            if Book.publicationDate <= date(1700, 1, 1):
                return RepositoryResponse(success=False, error_message=f"La fecha es incorrecta o es minima {Book.publicationDate}")
            
             # Validar si la totalPague  no es vacio
            if not Book.totalPague.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un valor válido")
            
             # Validar si la cantidad de inventario  no es vacio
            if not Book.quantityStock.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un valor válido")
            
             # Validar si la bookcover no es vacio
            if not Book.bookCover.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un dato válido")
            
            repo_response: RepositoryResponse = BookRepository(dbConnection.connection).insert(Book)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Update Books    
    async def updateBook(idBook: int, Book: Book):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el book es correcto
            if not Book.bookName.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")
            
             # Validar si la fecha de publicacion no este vacia 
            if Book.publicationDate <= date(1700, 1, 1):
                return RepositoryResponse(success=False, error_message=f"La fecha es incorrecta o es minima {Book.publicationDate}")
            
             # Validar si la totalPague  no es vacio
            if not Book.totalPague.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un valor válido")
            
             # Validar si la cantidad de inventario  no es vacio
            if not Book.quantityStock.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un valor válido")
            
            
             # Validar si la bookcover no es vacio
            if not Book.bookCover.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un dato válido")
            
            
            repo_response: RepositoryResponse = BookRepository(dbConnection.connection).update(idBook, Book)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
    #Delete Book    
    async def deleteBook(idBook: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = BookRepository(dbConnection.connection).delete(idBook)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Active Book    
    async def activeBook(idBook: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = BookRepository(dbConnection.connection).activate(idBook)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")