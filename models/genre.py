from pydantic import BaseModel
from typing import Optional

#Create model to Genre object
class Genre(BaseModel):

    idGenre: int = 0
    nameGenre: str = ""
    statusGenre: bool = True
