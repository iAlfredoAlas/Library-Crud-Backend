from fastapi import APIRouter, Header
from models.userAuth import UserAuth
from services.JWTService import JWTervice
from fastapi.responses import JSONResponse

#Create route
JWTRouter = APIRouter()

@JWTRouter.post("/login", tags=["Authentication"])
async def login(User: UserAuth):
    response = await JWTervice.Login(User)
    return JSONResponse(content=response.content)
    
    
@JWTRouter.post("/Verify/Token", tags=["Authentication"])
async def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    test = await JWTervice.Validate(token)
    return JSONResponse(content=test.content)