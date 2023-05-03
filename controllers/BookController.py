#Requeried imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional

from services.BookService import BookService
from models.repositoryResponse import RepositoryResponse
from models.book import Book

#CReate route
BookRouter = APIRouter()

#This controller can be uses like this "/Book?page=2&limit=20"
@BookRouter.get("/Book", tags=["Book"], summary="To add pagination use '/Book?page=1&limit=10&actives=True'")
async def getBooks(page: Optional[int] = 1, limit: Optional[int] = 10, actives: Optional[bool] = False):

    bookResult:RepositoryResponse = await BookService.getAuthor(page, limit, actives)
    
    if bookResult.success:
        return JSONResponse(bookResult.content)
    else:
        return JSONResponse(bookResult.error_message, status_code=400)

#Controller to get authors by id    
@BookRouter.get("/Book/{idBook}", tags=["Book"])
async def getBooksById(idBook: int):
    
    bookResult:RepositoryResponse = await BookService.getBookById(idBook)
    
    if bookResult.success:
        return JSONResponse(bookResult.content)
    else:
        return JSONResponse(bookResult.error_message, status_code=400)