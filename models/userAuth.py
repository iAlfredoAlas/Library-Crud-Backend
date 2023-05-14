from pydantic import BaseModel

class UserAuth(BaseModel):
    userName: str
    carnet: str