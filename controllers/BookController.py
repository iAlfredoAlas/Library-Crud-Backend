#Requeried imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional

from services.BookService import BookService
from models.repositoryResponse import RepositoryResponse
from models.book import Book

#Create route
BookRouter = APIRouter()

#This controller can be uses like this "/Book?page=2&limit=20"
@BookRouter.get("/Book", tags=["Book"], summary="To add pagination use '/Book?page=1&limit=10&actives=True'")
async def getBooks(page: Optional[int] = 1, limit: Optional[int] = 10, actives: Optional[bool] = False):

    BookResult:RepositoryResponse = await BookService.getBook(page, limit, actives)
    
    if BookResult.success:
        return JSONResponse(BookResult.content)
    else:
        return JSONResponse(BookResult.error_message, status_code=400)

#Controller to get Books by id    
@BookRouter.get("/Book/{idBook}", tags=["Book"])
async def getBooksById(idBook: int):
    
    BookResult:RepositoryResponse = await BookService.getBookById(idBook)
    
    if BookResult.success:
        return JSONResponse(BookResult.content)
    else:
        return JSONResponse(BookResult.error_message, status_code=400)
    
#Controller to post new Book    
@BookRouter.post("/Book", tags=["Book"])
async def postBook(Book: Book):
    BookResult:RepositoryResponse = await BookService.insertBook(Book)
    
    if BookResult.success:
        return JSONResponse(f"Book {Book.bookName} successfully added")
    else:
        return JSONResponse(BookResult.error_message, status_code=400)

#Controller to edit Book
@BookRouter.put("/Book/{idBook}", tags=["Book"])
async def putBook(idBook: int, Book: Book):
    BookResult:RepositoryResponse = await BookService.updateBook(idBook, Book)
    
    if BookResult.success:
        return JSONResponse(f"Book {Book.bookName} successfully edited")
    else:
        return JSONResponse(BookResult.error_message, status_code=400)

#Controller to delete Book    
@BookRouter.delete("/Book/{idBook}", tags=["Book"])
async def deleteBook(idBook: int):
    BookResult:RepositoryResponse = await BookService.deleteBook(idBook)
    
    if BookResult.success:
        return JSONResponse(f"Book with Id {idBook} successfully deleted")
    else:
        return JSONResponse(BookResult.error_message, status_code=400)
    
#Controller to activate Book    
@BookRouter.put("/Book/Activate/{idBook}", tags=["Book"])
async def activateBook(idBook: int):
    BookResult:RepositoryResponse = await BookService.activeBook(idBook)
    
    if BookResult.success:
        return JSONResponse(f"Book with Id {idBook} successfully activated")
    else:
        return JSONResponse(BookResult.error_message, status_code=400)