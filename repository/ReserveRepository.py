import mysql.connector
from models.reserve import Reserve
from models.repositoryResponse import RepositoryResponse

#Class of ReserveRepository
class ReserveRepository:
    
    #Initialization of the ReserveRepository
    def __init__(self, connection):
        self.connection = connection

    #Method getAll Reserves
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
    
    #Method getAllActivates
    def getAllActives(self, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT r.idReservation, r.dateReservation, r.statusReservation, r.idBook , b.bookName, r.idEmployee, e.nameEmployee, r.idUser, u.nameUser FROM Reserve r LEFT JOIN Book b ON r.idBook = b.idBook LEFT JOIN Employee e ON r.idEmployee = e.idEmployee LEFT JOIN User u ON r.idUser = u.idUser WHERE statusReservation = 1 LIMIT %s OFFSET %s;", (limit, offset))

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
    
    #Method getById Reserve
    def getById(self, idReserve: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT r.idReservation, r.dateReservation, r.statusReservation, r.idBook , b.bookName, r.idEmployee, e.nameEmployee, r.idUser, u.nameUser FROM Reserve r LEFT JOIN Book b ON r.idBook = b.idBook LEFT JOIN Employee e ON r.idEmployee = e.idEmployee LEFT JOIN User u ON r.idUser = u.idUser WHERE idReservation = %s LIMIT %s OFFSET %s;", (limit, offset))
        row = cursor.fetchone()
        if row:
            reserves = [
                {
                "idReserve": row[0],
                "dateReservation": str(row[1]),
                "statusReserve": row[2],
                "idBook": row[3],
                "Book": {
                    "bookName": row[4]
                },
                "idEmploye": row[5],
                "Employee": {
                    "nameEmployee": row[6]
                },
                "idUser": row[7],
                "User": {
                    "nameUser": row[8]
                }
            }
        ]
            return RepositoryResponse(reserves)
        else:
            return RepositoryResponse(success=False, error_message="Reserve not found")
        
    #Insert new reserve    
    def insert(self, reserve: Reserve):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Reserve WHERE idUser = %s", (reserve.idUser,))

        if cursor.fetchone():
            return RepositoryResponse(success=False, error_message="This user already has a reservation")
        else:
            try:
                cursor.execute("INSERT INTO Reserve (dateReservation, statusReservation, idBook, idEmployee, idUSer) VALUES (%s, %s, %s, %s, %s)", (reserve.dateReservation, reserve.statusReserve, reserve.idBook, reserve.idEmployee, reserve.idUser))
                self.connection.commit()
                return RepositoryResponse(success=True)
            except mysql.connector.Error as error:
                return RepositoryResponse(success=False, error_message="Can not insert Reserve, %s" % str(error))
            
    #Method update Authrs
    def update(self, idReserve: int, reserve: Reserve):
        cursor = self.connection.cursor()
        try:
            # Verificar si existe un autor con el mismo nombre
            cursor.execute("SELECT * FROM Reserve WHERE dateReservation = %s AND idReserve != %s", (reserve.dateReservation, idReserve))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A reserve with this name already exists")

            #Update Reserve
            cursor.execute("UPDATE Reserve SET dateReservatio = %s, statusReservation = %s, idBook = %s, idEmployee = %s, idUser = %s WHERE idReserve = %s", (reserve.dateReservation, reserve.statusReserve, reserve.idBook, reserve.idEmployee, reserve.idUser, reserve.idReservation))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="Reserve didn't change or reserve with id %s not found" % reserve.idReservation)
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not updtae Reserve, %s" % str(error))
    
    #Method delete Reserve   
    def delete(self, idReservation: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe una reserve con ese idReserve
            cursor.execute("SELECT * FROM Reserve WHERE idReservation = %s and statusReservation = 0", (idReservation,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A reserve with this Id has already been deleted")

            cursor.execute("UPDATE Reserve SET statusReservation = 0 WHERE idReservation = %s", (idReservation,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Reserve with id %s not found" % idReservation)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not delete Reserve, %s" % str(error))
        
    #Method activate Reserve   
    def activate(self, idReservation: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe una reserve con ese idReserve
            cursor.execute("SELECT * FROM Reserve WHERE idReservation = %s and statusReservation = 1", (idReservation,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A reserve with this Id has already been activated")

            cursor.execute("UPDATE Reserve SET statusReservation = 1 WHERE idReservation = %s", (idReservation,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Reserve with id %s not found" % idReservation)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not activate Reserve, %s" % str(error))