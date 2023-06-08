from models.userAuth import UserAuth
from models.repositoryResponse import RepositoryResponse

from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from dotenv import load_dotenv
from os import getenv
import json


def expire_date(minutes: int):
    date = datetime.now()
    new_date = date+timedelta(minutes=minutes)
    return new_date

def write_token(data:dict):
    token_expiration = int(getenv("TOKEN_EXPIRATION"))
    token = encode(payload={**data, "exp":expire_date(token_expiration)},key=getenv("SECRET"), algorithm="HS256")
    return token

def validate_token(token, output = False):
    try:
        return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return "Invalid token"
    except exceptions.ExpiredSignatureError:
        return "Token expired"

class JWTRepository:

     #Initialization of the EditorialRepository
    def __init__(self, connection):
        self.connection = connection

    def login(self, User: UserAuth):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) as count_employee FROM Employee WHERE nameEmployee = %s AND employeeNumber = %s", (User.userName, User.carnet))
        result = cursor.fetchone()

        if(result[0] == 1):
            return RepositoryResponse(write_token(User.dict()))
        else:
            return RepositoryResponse(success=False, error_message="Can not insert editorial, %s")
        
    def Validate(self,token):
        return RepositoryResponse(validate_token(token))