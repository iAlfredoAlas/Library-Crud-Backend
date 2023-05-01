from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from typing import Optional
import pickle

from services.GenreService import GenreService
from models.repositoryResponse import RepositoryResponse
from models.genre import Genre

GenreRouter = APIRouter()

#ESTE METODO SE PUEDE USAR ASI "/Genre?page=2&limit=20"
@GenreRouter.get("/Genre", tags=["Genre"], summary="To add pagination use '/Genre?page=1&limit=10&actives=True'")
async def get_genres(page: Optional[int] = 1, limit: Optional[int] = 10, actives: Optional[bool] = False):
    
    genresResult:RepositoryResponse = await GenreService.get_genres(page, limit, actives)
    
    if genresResult.success:
        return JSONResponse(genresResult.content)
    else:
        return JSONResponse(genresResult.error_message, status_code=400)
    

@GenreRouter.get("/Genre/{idGenre}", tags=["Genre"])
async def get_genres_by_id(idGenre: int):
    genresResult:RepositoryResponse = await GenreService.get_genre_by_id(idGenre)
    
    if genresResult.success:
        return JSONResponse(genresResult.content)
    else:
        return JSONResponse(genresResult.error_message, status_code=400)
    
@GenreRouter.post("/Genre", tags=["Genre"])
async def post_genre(Genre: Genre):
    genresResult:RepositoryResponse = await GenreService.insert_genre(Genre)
    
    if genresResult.success:
        return JSONResponse(f"Genero {Genre.nameGenre} agregado correctamente")
    else:
        return JSONResponse(genresResult.error_message, status_code=400)
    

@GenreRouter.put("/Genre/{idGenre}", tags=["Genre"])
async def put_genre(idGenre: int, Genre: Genre):
    genresResult:RepositoryResponse = await GenreService.update_genre(idGenre, Genre)
    
    if genresResult.success:
        return JSONResponse(f"Genero {Genre.nameGenre} editado correctamente")
    else:
        return JSONResponse(genresResult.error_message, status_code=400)
    

@GenreRouter.delete("/Genre/{idGenre}", tags=["Genre"])
async def delete_genre(idGenre: int):
    genresResult:RepositoryResponse = await GenreService.delete_genre(idGenre)
    
    if genresResult.success:
        return JSONResponse(f"Genero con Id {idGenre} fue eliminado correctamente")
    else:
        return JSONResponse(genresResult.error_message, status_code=400)
    

@GenreRouter.put("/Genre/Activate={idGenre}", tags=["Genre"])
async def activate_genre(idGenre: int):
    genresResult:RepositoryResponse = await GenreService.delete_genre(idGenre)
    
    if genresResult.success:
        return JSONResponse(f"Genero con Id {idGenre} fue eliminado correctamente")
    else:
        return JSONResponse(genresResult.error_message, status_code=400)