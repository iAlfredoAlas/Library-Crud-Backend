#Imports
from pydantic import BaseModel
from datetime import date
#Import instances
from author import Author
from editorial import Editorial
from genre import Genre
from rack import Rack

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
