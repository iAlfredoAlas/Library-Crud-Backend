#Requerid imports
from services.dbContext import DbContext
from repository.UserRepository import UserRepository
from models.repositoryResponse import RepositoryResponse
from models.user import User
import re

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
            # Validar si el correo electrónico es válido
            if not re.match(r"[^@]+@[^@]+\.[^@]+", User.emailUser):
                return RepositoryResponse(success=False, error_message="Correo electrónico inválido")

            # Validar si el nombre del usuario es correcto
            if not User.nameUser.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un nombre de usuario válido")
            
            # Validar si el carnet del usuario no es vacio
            if not User.carnetUser.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un carnet de usuario válido")
            
            # Validar si el numero de telefono es correcto
            if not User.phoneUser.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un telefono  válido")

            repo_response: RepositoryResponse = UserRepository(dbConnection.connection).insert(User)
            return repo_response
        else:
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        

    #Update Users    
    async def updateUser(idUser: int, User: User):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            # Validar si el correo electrónico es válido
            if not re.match(r"[^@]+@[^@]+\.[^@]+", User.emailUser):
                return RepositoryResponse(success=False, error_message="Correo electrónico inválido")

            # Validar si el nombre del usuario es correcto
            if not User.nameUser.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un nombre de usuario válido")
            
             # Validar si el carnet del usuario no es vacio
            if not User.carnetUser.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un carnet de usuario válido")
            
            # Validar si el numero de telefono es correcto
            if not User.phoneUser.strip():
                return RepositoryResponse(success=False, error_message="No se ha proporcionado un telefono  válido")

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
   