#Requerid imports
from services.dbContext import DbContext
from repository.ReserveRepository import ReserveRepository
from models.repositoryResponse import RepositoryResponse
from models.reserve import Reserve
from datetime import date

#Class of BookService
class ReserveService:

    #Pagination to Reserve
    async def getReserve(page: int, limit: int, actives: bool):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = ReserveRepository(dbConnection.connection).getAll(page, limit) if not actives else ReserveRepository(dbConnection.connection).getAllActives(page, limit)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    #Get Reserve by id    
    async def getReserveById(idReservation: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = ReserveRepository(dbConnection.connection).getById(idReservation)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    #Insert Reserves    
    async def insertReserve(Reserve: Reserve):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si la reserve es correcto
            if not Reserve.dateReservation.split():
                return RepositoryResponse(success=False, error_message=f"No contiene fecha o va vacio")
            
            repo_response: RepositoryResponse = ReserveRepository(dbConnection.connection).insert(Reserve)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Update Books    
    async def updateReserve(idReservation: int, Reserve: Reserve):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el book es correcto
            if not Reserve.dateReservation.split():
                return RepositoryResponse(success=False, error_message=f"No contiene fecha o va vacio")
            
            repo_response: RepositoryResponse = ReserveRepository(dbConnection.connection).update(idReservation, Reserve)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Delete Book    
    async def deleteBook(idReservation: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = ReserveRepository(dbConnection.connection).delete(idReservation)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Active Book    
    async def activeBook(idReservation: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = ReserveRepository(dbConnection.connection).activate(idReservation)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")