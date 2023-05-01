from services.dbContext import DbContext
from repository.RackRepository import RackRepository
from models.repositoryResponse import RepositoryResponse
from models.rack import Rack

#Class of RackRepository
class RackService:

    async def get_racks(page: int, limit: int, actives: bool):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = RackRepository(dbConnection.connection).get_all(page, limit) if not actives else RackRepository(dbConnection.connection).get_all_actives(page, limit)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def get_rack_by_id(idRack: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:
            repo_response: RepositoryResponse = RackRepository(dbConnection.connection).get_by_id(idRack)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def insert_rack(Rack: Rack):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el rack es correcto
            if not Rack.nameRack.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")

            repo_response: RepositoryResponse = RackRepository(dbConnection.connection).insert(Rack)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def update_rack(idRack: int, Rack: Rack):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            #Validar si el rack es correcto
            if not Rack.nameRack.split():
                return RepositoryResponse(success=False, error_message=f"No contiene nombre o va vacio")
            if Rack.levels < 1:
                return RepositoryResponse(success=False, error_message=f"Niveles del Rack invalidos {Rack.levels}")

            repo_response: RepositoryResponse = RackRepository(dbConnection.connection).update(idRack, Rack)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def delete_rack(idRack: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = RackRepository(dbConnection.connection).delete(idRack)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")
        
    async def Activate_rack(idRack: int):
        dbConnection = DbContext().connect()

        if dbConnection.success:

            repo_response: RepositoryResponse = RackRepository(dbConnection.connection).activate(idRack)
            return repo_response
        else: 
            return RepositoryResponse(success=False, error_message=f"Failed to connect: {dbConnection.error_message}")