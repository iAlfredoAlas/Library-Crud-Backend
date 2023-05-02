from pydantic import BaseModel
from typing import Optional

class Rack(BaseModel):
    
    idRack: int = 0
    nameRack: str = ""
    levels: int = 0
    statusRack: bool = True
