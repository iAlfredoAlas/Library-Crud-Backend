#Requeried imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional

from services.UserService import UserService
from models.repositoryResponse import RepositoryResponse
from models.user import User

#Create route
UserRouter = APIRouter()

#This controller can be uses like this "/User?page=2&limit=20"
@UserRouter.get("/User", tags=["User"], summary="To add pagination use '/User?page=1&limit=10&actives=True'")
async def getUser(page: Optional[int] = 1, limit: Optional[int] = 10, actives: Optional[bool] = False):

    userResult:RepositoryResponse = await UserService.getUser(page, limit, actives)
    
    if userResult.success:
        return JSONResponse(userResult.content)
    else:
        return JSONResponse(userResult.error_message, status_code=400)

#Controller to get user by id    
@UserRouter.get("/User/{idUSer}", tags=["User"])
async def getUsersById(idUser: int):
    
    userResult:RepositoryResponse = await UserService.getUserById(idUser)
    
    if userResult.success:
        return JSONResponse(userResult.content)
    else:
        return JSONResponse(userResult.error_message, status_code=400)

#Controller to post new User    
@UserRouter.post("/User", tags=["User"])
async def postUser(User: User):
    userResult:RepositoryResponse = await UserService.insertUser(User)
    
    if userResult.success:
        return JSONResponse(f"User {User.nameUser} successfully added")
    else:
        return JSONResponse(userResult.error_message, status_code=400)

#Controller to edit User
@UserRouter.put("/User/{idUser}", tags=["User"])
async def putUsere(idUser: int, User: User):
    userResult:RepositoryResponse = await UserService.updateUser(idUser, User)
    
    if userResult.success:
        return JSONResponse(f"User {User.nameUser} successfully edited")
    else:
        return JSONResponse(userResult.error_message, status_code=400)

#Controller to delete User    
@UserRouter.delete("/User/{idUser}", tags=["User"])
async def deleteUser(idUser: int):
    userResult:RepositoryResponse = await UserService.deleteUser(idUser)
    
    if userResult.success:
        return JSONResponse(f"User with Id {idUser} successfully deleted")
    else:
        return JSONResponse(userResult.error_message, status_code=400)
    
#Controller to activate User    
@UserRouter.put("/User/Activate/{idUser}", tags=["User"])
async def activateUsere(idUser: int):
    userResult:RepositoryResponse = await UserService.activeUser(idUser)
    
    if userResult.success:
        return JSONResponse(f"User with Id {idUser} successfully activated")
    else:
        return JSONResponse(userResult.error_message, status_code=400)
User