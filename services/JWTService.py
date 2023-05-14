from services.dbContext import DbContext
from repository.JWTRepository import JWTRepository
from models.repositoryResponse import RepositoryResponse
from models.userAuth import UserAuth
from datetime import date

#Class of JWTervice
class JWTervice:
       
    async def Login(User: UserAuth):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response = JWTRepository(dbConnection.connection).login(User)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def Validate(token: str):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response = JWTRepository(dbConnection.connection).Validate(token)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")