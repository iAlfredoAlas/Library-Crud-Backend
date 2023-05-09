#Imports
from pydantic import BaseModel
from datetime import date
from typing import Optional



#Create model to Author object
class Author(BaseModel):

    idAuthor: Optional [int] =  None
    nameAuthor: str = ""
    countryBirth: str = ""
    dateBorn: date = date(1700, 1, 1)
    statusAuthor: bool = True