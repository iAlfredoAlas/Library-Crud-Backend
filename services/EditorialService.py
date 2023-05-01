from services.dbContext import DbContext
from repository.EditorialRepository import EditorialRepository
from models.repositoryResponse import RepositoryResponse
from models.editorial import Editorial
from datetime import date

#Class of EditorialService
class EditorialService:

    async def getEditorial(page: int, limit: int, actives: bool):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = EditorialRepository(dbConnection.connection).getAll(page, limit) if not actives else EditorialRepository(dbConnection.connection).getAllActives(page, limit)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def getEditorialById(idEditorial: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = EditorialRepository(dbConnection.connection).getById(idEditorial)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def insertEditorial(Editorial: Editorial):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el editorial es correcto
            if not Editorial.nameEditorial.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")
            if Editorial.dateAdd <= date(1900, 1, 1):
                return RepositoryResponse(success=False, error_message=f"La fecha es incorrecta o es minima {Editorial.dateAdd}")

            repo_response: RepositoryResponse = EditorialRepository(dbConnection.connection).insert(Editorial)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def updateEditorial(idEditorial: int, Editorial: Editorial):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el editorial es correcto
            if not Editorial.nameEditorial.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")
            if Editorial.dateAdd <= date(1900, 1, 1):
                return RepositoryResponse(success=False, error_message=f"La fecha es incorrecta o es minima {Editorial.dateAdd}")

            repo_response: RepositoryResponse = EditorialRepository(dbConnection.connection).update(idEditorial, Editorial)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def deleteEditorial(idEditorial: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = EditorialRepository(dbConnection.connection).delete(idEditorial)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def activateEditorial(idEditorial: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = EditorialRepository(dbConnection.connection).activate(idEditorial)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")