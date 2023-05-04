#Imports
from pydantic import BaseModel
from datetime import date

#Import instances
from models.book import Book
from models.employee import Employee
from models.user import User

class Reserve:

    idReservation: int = 0
    dateReservation: date = date(2023, 1, 1)
    idBook: int = 0
    book: Book = None
    idEmployee: int = 0
    employee: Employee = None
    idUser: int = 0
    user: User = None