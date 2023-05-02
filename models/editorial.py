from pydantic import BaseModel
from datetime import date

class Editorial(BaseModel):

    idEditorial: int = 0
    nameEditorial: str = ""
    dateAdd: date = date(1700, 1, 1)
    statusEditorial: bool = True
