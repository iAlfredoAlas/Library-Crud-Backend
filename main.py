from models.books import Books
from models.editorial import Editorial
from models.author import Author
from models.genre import Genre
from models.rack import Rack
from models.employee import Employee
from models.user import User
from models.reserve import Reserve
from datetime import datetime
from services.dbContext import DbConnection, DbContext
from repository.GenreRepository import GenreRepository


dbContext = DbContext()
dbContext.setDefaultContext()

dbConnection = dbContext.connect()

if dbConnection.success:
    print("Connected to database!")

    #Uso de repositorio Genre Get All
    repoGetResult = GenreRepository(dbConnection.connection).get_all()
    all_genres = repoGetResult.content if repoGetResult.success else []
    for genre in all_genres:
        print(genre.getIdGenre(), genre.getNameGenre())

    #Uso de repositorio Genre Get By Id
    repoGetByIdResult = GenreRepository(dbConnection.connection).get_by_id(1)
    print(repoGetByIdResult.content.getIdGenre(), repoGetByIdResult.content.getNameGenre()) if repoGetResult.success else print(repoGetResult.error_message)

    #Uso de repositorio Genre Insert
    genre = Genre(1,'Ejemplo1')
    repoInsertResult = GenreRepository(dbConnection.connection).insert(genre)
    print("Insertado") if repoInsertResult.success else print("No Insertado "+repoInsertResult.error_message)

    #Uso de repositorio Genre Update
    genre = Genre(3, 'Noooooo')
    repoUpdateResult = GenreRepository(dbConnection.connection).update(genre)
    print("Actualizado") if repoUpdateResult.success else print("No Actualizado "+repoUpdateResult.error_message)

    #Uso de repositorio Genre Delete
    repoDeleteResult = GenreRepository(dbConnection.connection).delete(2)
    print("Eliminado") if repoDeleteResult.success else print("No eliminado "+repoDeleteResult.error_message)

    
else:
    print(f"Failed to connect: {dbConnection.error_message}")
