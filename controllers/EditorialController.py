from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional

from services.EditorialService import EditorialService
from models.repositoryResponse import RepositoryResponse
from models.editorial import Editorial

EditorialRouter = APIRouter()

#ESTE METODO SE PUEDE USAR ASI "/Editorial?page=2&limit=20"
@EditorialRouter.get("/Editorial", tags=["Editorial"], summary="To add pagination use '/Editorial?page=1&limit=10&actives=True'")
async def getEditorial(page: Optional[int] = 1, limit: Optional[int] = 10, actives: Optional[bool] = False):
    
    editorialResult:RepositoryResponse = await EditorialService.getEditorial(page, limit, actives)
    
    if editorialResult.success:
        print(editorialResult.content)
        return JSONResponse(editorialResult.content)
    else:
        return JSONResponse(editorialResult.error_message, status_code=400)
    
@EditorialRouter.get("/Editorial/{idEditorial}", tags=["Editorial"])
async def getEditorialById(idEditorial: int):
    editorialResult:RepositoryResponse = await EditorialService.getEditorialById(idEditorial)
    
    if editorialResult.success:
        return JSONResponse(editorialResult.content)
    else:
        return JSONResponse(editorialResult.error_message, status_code=400)
    
@EditorialRouter.post("/Editorial", tags=["Editorial"])
async def postEditorial(Editorial: Editorial):
    editorialResult:RepositoryResponse = await EditorialService.insertEditorial(Editorial)
    
    if editorialResult.success:
        return JSONResponse(f"Genero {Editorial.nameEditorial} agregado correctamente")
    else:
        return JSONResponse(editorialResult.error_message, status_code=400)
    
@EditorialRouter.put("/Editorial/{idEditorial}", tags=["Editorial"])
async def putEditorial(idEditorial: int, Editorial: Editorial):
    editorialResult:RepositoryResponse = await EditorialService.updateEditorial(idEditorial, Editorial)
    
    if editorialResult.success:
        return JSONResponse(f"Genero {Editorial.nameEditorial} editado correctamente")
    else:
        return JSONResponse(editorialResult.error_message, status_code=400)
    
@EditorialRouter.delete("/Editorial/{idEditorial}", tags=["Editorial"])
async def deleteEditorial(idEditorial: int):
    editorialResult:RepositoryResponse = await EditorialService.deleteEditorial(idEditorial)
    
    if editorialResult.success:
        return JSONResponse(f"Genero con Id {idEditorial} fue eliminado correctamente")
    else:
        return JSONResponse(editorialResult.error_message, status_code=400)
    
@EditorialRouter.put("/Editorial/Activate/{idEditorial}", tags=["Editorial"])
async def activateEditorial(idEditorial: int):
    editorialResult:RepositoryResponse = await EditorialService.activateEditorial(idEditorial)
    
    if editorialResult.success:
        return JSONResponse(f"Genero con Id {idEditorial} fue Activado correctamente")
    else:
        return JSONResponse(editorialResult.error_message, status_code=400)