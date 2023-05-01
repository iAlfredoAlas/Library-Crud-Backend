from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional

from services.RackService import RackService
from models.repositoryResponse import RepositoryResponse
from models.rack import Rack

RackRouter = APIRouter()

#ESTE METODO SE PUEDE USAR ASI "/Rack?page=2&limit=20"
@RackRouter.get("/Rack", tags=["Rack"], summary="To add pagination use '/Rack?page=1&limit=10&actives=True'")
async def get_rack(page: Optional[int] = 1, limit: Optional[int] = 10, actives: Optional[bool] = False):
    
    racksResult:RepositoryResponse = await RackService.get_racks(page, limit, actives)
    
    if racksResult.success:
        return JSONResponse(racksResult.content)
    else:
        return JSONResponse(racksResult.error_message, status_code=400)
    
@RackRouter.get("/Rack/{idRack}", tags=["Rack"])
async def get_rack_by_id(idRack: int):
    rackResult:RepositoryResponse = await RackService.get_rack_by_id(idRack)
    
    if rackResult.success:
        return JSONResponse(rackResult.content)
    else:
        return JSONResponse(rackResult.error_message, status_code=400)
    
@RackRouter.post("/Rack", tags=["Rack"])
async def post_rack(Rack: Rack):
    rackResult:RepositoryResponse = await RackService.insert_rack(Rack)
    
    if rackResult.success:
        return JSONResponse(f"Rack {Rack.nameRack} agregado correctamente")
    else:
        return JSONResponse(rackResult.error_message, status_code=400)
    
@RackRouter.put("/Rack/{idRack}", tags=["Rack"])
async def put_rack(idRack: int, Rack: Rack):
    rackResult:RepositoryResponse = await RackService.update_rack(idRack, Rack)
    
    if rackResult.success:
        return JSONResponse(f"Rack {Rack.nameRack} editado correctamente")
    else:
        return JSONResponse(rackResult.error_message, status_code=400)
    
@RackRouter.delete("/Rack/{idRack}", tags=["Rack"])
async def delete_rack(idRack: int):
    rackResult:RepositoryResponse = await RackService.delete_rack(idRack)
    
    if rackResult.success:
        return JSONResponse(f"Rack con Id {idRack} fue eliminado correctamente")
    else:
        return JSONResponse(rackResult.error_message, status_code=400)
    
@RackRouter.put("/Rack/Activate/{idRack}", tags=["Rack"])
async def activate_rack(idRack: int):
    rackResult:RepositoryResponse = await RackService.Activate_rack(idRack)
    
    if rackResult.success:
        return JSONResponse(f"Rack con Id {idRack} fue Activado correctamente")
    else:
        return JSONResponse(rackResult.error_message, status_code=400)