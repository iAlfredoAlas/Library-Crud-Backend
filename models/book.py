#Imports
from pydantic import BaseModel
from datetime import date
#Import instances
from models.author import Author
from models.editorial import Editorial
from models.genre import Genre
from models.rack import Rack

#Create model to Book object
class Book(BaseModel):

    idBook: int = 0
    bookName: str = ""
    publicationDate: date = date(1700, 1, 1)
    totalPague: int = ""
    quantityStock: int = ""
    bookCover: str = ""
    statusBook: bool = True
    idAuthor: int = 0
    author: Author = None
    idEditorial: int = 0
    editorial: Editorial = None
    idGenre: int = 0
    genre: Genre = None
    idRack: int = 0
    rack: Rack = None
