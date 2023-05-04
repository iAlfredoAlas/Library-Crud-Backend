#Requeried imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional

from services.ReserveService import ReserveService 
from models.repositoryResponse import RepositoryResponse
from models.reserve import Reserve

#Create route
ReserveRouter = APIRouter()

#This controller can be uses like this "/Book?page=2&limit=20"
@ReserveRouter.get("/Reserve", tags=["Reserve"], summary="To add pagination use '/Reserve?page=1&limit=10&actives=True'")
async def getReserves(page: Optional[int] = 1, limit: Optional[int] = 10, actives: Optional[bool] = False):

    ReserveResult:RepositoryResponse = await ReserveService.getReserve(page, limit, actives)
    
    if ReserveResult.success:
        return JSONResponse(ReserveResult.content)
    else:
        return JSONResponse(ReserveResult.error_message, status_code=400)