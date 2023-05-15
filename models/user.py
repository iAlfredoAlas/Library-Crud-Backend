#Imports
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

#Create model to User object
class User(BaseModel):

    idUser: int = 0
    nameUser: str = ""
    carnetUser: str = ""
    emailUser: str = ""
    phoneUser: str = Field(default="00000000",min_length=8,max_length=11)
    statusUser: bool = True
