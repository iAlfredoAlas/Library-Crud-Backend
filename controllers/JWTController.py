from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Header
from pydantic import BaseModel, EmailStr

#Create route
JWTRouter = APIRouter()

def expire_date(days: int):
    date = datetime.now()
    new_date = date+timedelta(days)
    return new_date

def write_token(data:dict):
    token = encode(payload={**data, "exp":expire_date(1)},key=getenv("SECRET"), algorithm="HS256")
    return token

def validate_token(token, output = False):
    try:
        return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message":"Invalid token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message":"Token expired"}, status_code=401)
    
class UserAuth(BaseModel):
    userName: str
    carnet: str

@JWTRouter.post("/login", tags=["Authentication"])
def login(User: UserAuth):
    if(User.userName=="Alexis"):
        return write_token(User.dict())
    else:
        return JSONResponse(content={"error": "Usuario not found"}, status_code=404)
    
@JWTRouter.post("/Verify/Token", tags=["Authentication"])
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token)