import mysql.connector
from models.reserve import Reserve
from models.repositoryResponse import RepositoryResponse

#Class of ReserveRepository
class ReserveRepository:
    
    #Initialization of the ReserveRepository
    def __init__(self, connection):
        self.connection = connection

    def getAll(self, page: int, limit: int):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT r.idReservation, r.dateReservation, r.statusReservation, r.idBook , b.bookName, r.idEmployee, e.nameEmployee, r.idUser, u.nameUser FROM Reserve r LEFT JOIN Book b ON r.idBook = b.idBook LEFT JOIN Employee e ON r.idEmployee = e.idEmployee LEFT JOIN User u ON r.idUser = u.idUser LIMIT %s OFFSET %s;", (limit, offset))

        rows = cursor.fetchall()

        reserves = [
            {
                "idReserve": reserve[0],
                "dateReservation": str(reserve[1]),
                "statusReserve": reserve[2],
                "idBook": reserve[3],
                "Book": {
                    "bookName": reserve[4]
                },
                "idEmploye": reserve[5],
                "Employee": {
                    "nameEmployee": reserve[6]
                },
                "idUser": reserve[7],
                "User": {
                    "nameUser": reserve[8]
                }
            }

            for reserve in rows
            
        ]
        
        return RepositoryResponse(reserves)