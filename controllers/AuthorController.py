from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional

from services.AuthorService import GenreService
from models.repositoryResponse import RepositoryResponse
from models.genre import Genre