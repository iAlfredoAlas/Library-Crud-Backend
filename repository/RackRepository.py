import mysql.connector
from models.rack import Rack
from models.repositoryResponse import RepositoryResponse


class RackRepository:
    
    #Initialization of the RackRepository
    def __init__(self, connection):
        self.connection = connection

    def get_all(self, page: int, limit: int):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Rack LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        
        return RepositoryResponse(result)
    
    def get_all_actives(self, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Rack WHERE statusRack = 1 LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        
        return RepositoryResponse(result)
    
    def get_by_id(self, idRack: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Rack WHERE idRack = %s", (idRack,))
        row = cursor.fetchone()
        if row:
            column_names = [column[0] for column in cursor.description]
            rack_dict = dict(zip(column_names, row))
            return RepositoryResponse(rack_dict)
        else:
            return RepositoryResponse(success=False, error_message="Rack not found")
    
    def insert(self, rack: Rack):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Rack where nameRack = %s", (rack.nameRack,))

        if cursor.fetchone():
            return RepositoryResponse(success=False, error_message=f"Rack with the name {rack.nameRack} already exists")
        else:
            try:
                cursor.execute("INSERT INTO Rack (nameRack, levels, statusRack) VALUES (%s, %s, %s)", (rack.nameRack, rack.levels, rack.statusRack))
                self.connection.commit()
                return RepositoryResponse(success=True)
            except mysql.connector.Error as error:
                return RepositoryResponse(success=False, error_message="Can not insert rack, %s" % str(error))
            
    def update(self, idRack: int, rack: Rack):
        cursor = self.connection.cursor()
        try:
            # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idRack FROM Rack WHERE nameRack = %s AND idRack != %s", (rack.nameRack, idRack))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A rack with this name already exists")

            # Actualizar el género
            cursor.execute("UPDATE Rack SET nameRack = %s, statusRack = %s WHERE idRack = %s", (rack.nameRack, rack.statusRack, idRack))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="Rack didn't change or rack with id %s not found" % rack.idRack)
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not update rack, %s" % str(error))
        
    def delete(self, idRack: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idRack FROM Rack WHERE idRack = %s and statusRack = 0", (idRack,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A rack with this Id has already been deleted")

            cursor.execute("UPDATE Rack SET statusRack = 0 WHERE idRack = %s", (idRack,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Rack with id %s not found" % idRack)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not delete rack, %s" % str(error))

    def activate(self, idRack: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idRack FROM Rack WHERE idRack = %s and statusRack = 1", (idRack,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A rack with this Id has already been Activate")

            cursor.execute("UPDATE Rack SET statusRack = 1 WHERE idRack = %s", (idRack,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Rack with id %s not found" % idRack)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not Activate rack, %s" % str(error))