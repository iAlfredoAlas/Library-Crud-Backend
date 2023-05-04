#Requerid imports
from services.dbContext import DbContext
from repository.ReserveRepository import ReserveRepository
from models.repositoryResponse import RepositoryResponse
from models.reserve import Reserve
from datetime import date

#Class of BookService
class ReserveService:

    #Pagination to Book
    async def getReserve(page: int, limit: int, actives: bool):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = ReserveRepository(dbConnection.connection).getAll(page, limit) if not actives else ReserveRepository(dbConnection.connection).getAllActives(page, limit)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")