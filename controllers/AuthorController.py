#Requeried imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional

from services.AuthorService import AuthorService
from models.repositoryResponse import RepositoryResponse
from models.author import Author

#Create route
AuthorRoute = APIRouter()

#This controller can be uses like this "/Author?page=2&limit=20"
@AuthorRoute.get("/Author", tags=["Author"], summary="To add pagination use '/Author?page=1&limit=10&actives=True'")
async def getAuthors(page: Optional[int] = 1, limit: Optional[int] = 10, actives: Optional[bool] = False):

    authorResult:RepositoryResponse = await AuthorService.getAuthor(page, limit, actives)
    
    if authorResult.success:
        return JSONResponse(authorResult.content)
    else:
        return JSONResponse(authorResult.error_message, status_code=400)

#Controller to get authors by id    
@AuthorRoute.get("/Author/{idAuthor}", tags=["Author"])
async def getAuthorsById(idAuthor: int):
    
    authorResult:RepositoryResponse = await AuthorService.getAuthorById(idAuthor)
    
    if authorResult.success:
        return JSONResponse(authorResult.content)
    else:
        return JSONResponse(authorResult.error_message, status_code=400)

#Controller to post new Author    
@AuthorRoute.post("/Author", tags=["Author"])
async def postAuthor(Author: Author):
    authorResult:RepositoryResponse = await AuthorService.insertAuthor(Author)
    
    if authorResult.success:
        return JSONResponse(f"Author {Author.nameAuthor} successfully added")
    else:
        return JSONResponse(authorResult.error_message, status_code=400)

#Controller to edit Author
@AuthorRoute.put("/Author/{idAuthor}", tags=["Author"])
async def putAuthor(idAuthor: int, Author: Author):
    authorResult:RepositoryResponse = await AuthorService.updateAuthor(idAuthor, Author)
    
    if authorResult.success:
        return JSONResponse(f"Author {Author.nameAuthor} successfully edited")
    else:
        return JSONResponse(authorResult.error_message, status_code=400)

#Controller to delete Author    
@AuthorRoute.delete("/Author/{idAuthor}", tags=["Auhtor"])
async def deleteAuthor(idAuthor: int):
    authorResult:RepositoryResponse = await AuthorService.deleteAuthor(idAuthor)
    
    if authorResult.success:
        return JSONResponse(f"Author with Id {idAuthor} successfully deleted")
    else:
        return JSONResponse(authorResult.error_message, status_code=400)
    
#Controller to activate Author    
@AuthorRoute.put("/Author/Activate/{idAuthor}", tags=["Author"])
async def activateAuthor(idAuthor: int):
    authorResult:RepositoryResponse = await AuthorService.activeAuthor(idAuthor)
    
    if authorResult.success:
        return JSONResponse(f"Auhtor with Id {idAuthor} successfully activated")
    else:
        return JSONResponse(authorResult.error_message, status_code=400)
