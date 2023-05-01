#Imports
from pydantic import BaseModel
from typing import Optional

#Create model to Author object
class Author(BaseModel):

    idAuthor: int = 0
    nameAuthor: str = ""
    countryBirth: str = ""
    dateBorn: str = ""