#FastAPI imports
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


#Implementación Swagger
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html

#route a otros controladores
from controllers.GenreController import GenreRouter as Genre
from controllers.RackController import RackRouter as Rack
from controllers.AuthorController import AuthorRouter as Author
from controllers.EditorialController import EditorialRouter as Editorial
from controllers.EmployeeController import EmployeeRouter as Employee
from controllers.UserController import UserRouter as User
from controllers.BookController import BookRouter as Book
from controllers.ReserveController import ReserveRouter as Reserve
from controllers.JWTController import JWTRouter as JWT
from controllers.JWTController import validate_token
from dotenv import load_dotenv


#Instancias y routes
app = FastAPI()
app.include_router(Genre)
app.include_router(Rack)
app.include_router(Author)
app.include_router(Editorial)
app.include_router(Employee)
app.include_router(User)
app.include_router(Book)
app.include_router(Reserve)
app.include_router(JWT)

load_dotenv()

async def jwtMiddleware(request: Request, call_next):  
    
    endpoints = ["Genre", "Author", "Book", "Editorial", "Rack", "User", "Employee"]

    for endpoint in endpoints:
        if endpoint in str( request.url):

            auth_header = request.headers.get("Authorization")
            if auth_header:
                response = validate_token(auth_header.split(" ")[1])
                if not isinstance(response, JSONResponse):
                    return await call_next(request)
                else:
                    return JSONResponse(content={"error":"Necesita Autenticarse"}, status_code=401)
            else:
                return JSONResponse(content={"error":"Necesita Autenticarse"}, status_code=401)

    return await call_next(request)
    

app.middleware("http")(jwtMiddleware)

# Configurar el middleware CORS para permitir todas las solicitudes
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Swagger documentation
@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return JSONResponse(get_openapi(title="Parcial 80%", version="1.0.0", routes=app.routes))
@app.get("/docs", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Documentación")

#Endpoints
@app.get("/", include_in_schema=False)
async def root():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Documentación")

#uvicorn main:app --reload