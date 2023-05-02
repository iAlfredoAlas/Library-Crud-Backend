#Imports
from pydantic import BaseModel
from datetime import date
from typing import Optional

#Create model to User object
class User(BaseModel):

    idUser: int = 0
    nameUser: str = ""
    carnetUser: str = ""
    emailUser: str = ""
    phoneUser: str = ""
    statusUser: bool = True
