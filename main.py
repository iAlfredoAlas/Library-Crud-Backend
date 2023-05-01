#FastAPI imports
from fastapi import FastAPI
from fastapi.responses import JSONResponse

#Implementación Swagger
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html

#route a otros controladores
from controllers.GenreController import GenreRouter as Genre
from controllers.RackController import RackRouter as Rack
from controllers.AuthorController import AuthorRoute as Author

#Instancias y routes
app = FastAPI()
app.include_router(Genre)
app.include_router(Rack)
app.include_router(Author)

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