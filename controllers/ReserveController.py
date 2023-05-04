#Requeried imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional

from services.ReserveService import ReserveService 
from models.repositoryResponse import RepositoryResponse
from models.reserve import Reserve

#Create route
ReserveRouter = APIRouter()

#This controller can be uses like this "/Reserve?page=2&limit=20"
@ReserveRouter.get("/Reserve", tags=["Reserve"], summary="To add pagination use '/Reserve?page=1&limit=10&actives=True'")
async def getReserves(page: Optional[int] = 1, limit: Optional[int] = 10, actives: Optional[bool] = False):

    ReserveResult:RepositoryResponse = await ReserveService.getReserve(page, limit, actives)
    
    if ReserveResult.success:
        return JSONResponse(ReserveResult.content)
    else:
        return JSONResponse(ReserveResult.error_message, status_code=400)
    
#Controller to get Reserves by id    
@ReserveRouter.get("/Reserve/{idReservation}", tags=["Reserve"])
async def getReservesById(idReservation: int):
    
    ReserveResult:RepositoryResponse = await ReserveService.getReserveById(idReservation)
    
    if ReserveResult.success:
        return JSONResponse(ReserveResult.content)
    else:
        return JSONResponse(ReserveResult.error_message, status_code=400)
    
#Controller to post new Reserve    
@ReserveRouter.post("/Reserve", tags=["Reserve"])
async def postReserve(Reserve: Reserve):
    ReserveResult:RepositoryResponse = await ReserveService.insertReserve(Reserve)
    
    if ReserveResult.success:
        return JSONResponse(f"Reserve {Reserve.idReservation} successfully added")
    else:
        return JSONResponse(ReserveResult.error_message, status_code=400)

#Controller to edit Reserve
@ReserveRouter.put("/Reserve/{idReservation}", tags=["Reserve"])
async def putReserve(idReservation: int, Reserve: Reserve):
    ReserveResult:RepositoryResponse = await ReserveService.updateReserve(idReservation, Reserve)
    
    if ReserveResult.success:
        return JSONResponse(f"Reserve {Reserve.idReservation} successfully edited")
    else:
        return JSONResponse(ReserveResult.error_message, status_code=400)

#Controller to delete Reserve    
@ReserveRouter.delete("/Reserve/{idReservation}", tags=["Reserve"])
async def deleteReserve(idReservation: int):
    ReserveResult:RepositoryResponse = await ReserveService.deleteReserve(idReservation)
    
    if ReserveResult.success:
        return JSONResponse(f"Reserve with Id {idReservation} successfully deleted")
    else:
        return JSONResponse(ReserveResult.error_message, status_code=400)
    
#Controller to activate Reserve    
@ReserveRouter.put("/Reserve/Activate/{idReservation}", tags=["Reserve"])
async def activateReserve(idReservation: int):
    ReserveResult:RepositoryResponse = await ReserveService.activeReserve(idReservation)
    
    if ReserveResult.success:
        return JSONResponse(f"Reserve with Id {idReservation} successfully activated")
    else:
        return JSONResponse(ReserveResult.error_message, status_code=400)