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


autor1 = Author(1, "Gabriel Garcia Marquez", "Colombia", datetime(1927, 3, 6))
editorial1 = Editorial(1, "Editorial A", datetime.now())
genre1 = Genre(1, "Novela")
rack1 = Rack(1, "A1")
libro1 = Books(1, "Cien años de soledad", datetime(1967, 5, 30), 471, 10, autor1.getId(), editorial1.getId(), genre1.getId(), rack1.getId())
print(libro1) # Libros(1, Cien años de soledad, 1967-05-30 00:00:00, 471, 10, 1, 1, 1, 1)

editorial1 = Editorial(1, "Editorial A", datetime.now())
print(editorial1) # Editorial(1, Editorial A, 2023

autor1 = Author(1, "Gabriel Garcia Marquez", "Colombia", datetime(1927, 3, 6))
print(autor1) # Autor(1, Gabriel Garcia Marquez, Colombia, 1927-03-06)  

genre1 = Genre(1, "Fiction")
print(genre1) # Genre(1, Fiction)

rack1 = Rack(1, "A1")
print(rack1) # Rack(1, A1)

employee1 = Employee(1, "John Doe", "EMP1001")
print(employee1) # Employee(1, John Doe, EMP1001)

user1 = User(1, "John Smith", "123456", "johnsmith@example.com", "555-1234")
print(user1) # User(1, John Smith, 123456, johnsmith@example.com, 555-1234)

reserve1 = Reserve(1, 2, 3, 4)
print(reserve1) # Reserve(1, 2, 3, 4)

dbContext = DbContext()
dbContext.setDefaultContext()

dbConnection = dbContext.connect()

if dbConnection.success:
    print("Connected to database!")
else:
    print(f"Failed to connect: {dbConnection.error_message}")
