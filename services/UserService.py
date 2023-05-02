#Requerid imports
from services.dbContext import DbContext
from repository.UserRepository import UserRepository
from models.repositoryResponse import RepositoryResponse
from models.user import User

#Class of UserService
class UserService:

    #Pagination to User
    async def getUser(page: int, limit: int, actives: bool):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = UserRepository(dbConnection.connection).getAll(page, limit) if not actives else UserRepository(dbConnection.connection).getAllActives(page, limit)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    #Get User by id    
    async def getUserById(idUser: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = UserRepository(dbConnection.connection).getById(idUser)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Insert Users    
    async def insertUser(User: User):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el autor es correcto
            if not User.nameUser.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")

            repo_response: RepositoryResponse = UserRepository(dbConnection.connection).insert(User)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Update Users    
    async def updateUser(idUser: int, User: User):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el autor es correcto
            if not User.nameUser.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")

            repo_response: RepositoryResponse = UserRepository(dbConnection.connection).update(idUser, User)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Delete User    
    async def deleteUser(idUser: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = UserRepository(dbConnection.connection).delete(idUser)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")

    #Active User    
    async def activeUser(idUser: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = UserRepository(dbConnection.connection).activate(idUser)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
   