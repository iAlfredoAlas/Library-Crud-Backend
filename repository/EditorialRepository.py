import mysql.connector
from models.editorial import Editorial
from models.repositoryResponse import RepositoryResponse

#Class of EditorialRepository
class EditorialRepository:
    
    #Initialization of the EditorialRepository
    def __init__(self, connection):
        self.connection = connection

    def getAll(self, page: int, limit: int):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM editorial LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        
        return RepositoryResponse(result)
    
    def getAllActives(self, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM editorial WHERE statusEditorial = 1 LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        
        return RepositoryResponse(result)
    
    def getById(self, idEditorial: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM editorial WHERE idEditorial = %s", (idEditorial,))
        row = cursor.fetchone()
        if row:
            column_names = [column[0] for column in cursor.description]
            editorial_dict = dict(zip(column_names, row))
            return RepositoryResponse(editorial_dict)
        else:
            return RepositoryResponse(success=False, error_message="Editorial not found")

    def insert(self, editorial: Editorial):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM editorial WHERE nameEditorial = %s", (editorial.nameEditorial,))

        if cursor.fetchone():
            return RepositoryResponse(success=False, error_message="Editorial already exists")
        else:
            try:
                cursor.execute("INSERT INTO editorial (nameEditorial, dateAdd, statusEditorial) VALUES (%s, %s, %s)", (editorial.nameEditorial, editorial.dateAdd, editorial.statusEditorial))
                self.connection.commit()
                return RepositoryResponse(success=True)
            except mysql.connector.Error as error:
                return RepositoryResponse(success=False, error_message="Can not insert editorial, %s" % str(error))

    def update(self, idEditorial: int, editorial: Editorial):
        cursor = self.connection.cursor()
        try:
            # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idEditorial FROM editorial WHERE nameEditorial = %s AND idEditorial != %s", (editorial.nameEditorial, idEditorial))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="An Editorial with this name already exists")

            # Actualizar el género
            cursor.execute("UPDATE editorial SET nameEditorial = %s, dateAdd = %s, statusEditorial = %s WHERE idEditorial = %s", (editorial.nameEditorial, editorial.dateAdd, editorial.statusEditorial, idEditorial))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="Editorial didn't change or editorial with id %s not found" % editorial.idEditorial)
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not update editorial, %s" % str(error))

    def delete(self, idEditorial: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idEditorial FROM editorial WHERE idEditorial = %s and statusEditorial = 0", (idEditorial,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="An editorial with this Id has already been deleted")

            cursor.execute("UPDATE editorial SET statusEditorial = 0 WHERE idEditorial = %s", (idEditorial,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Editorial with id %s not found" % idEditorial)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not Delete editorial, %s" % str(error))

    def activate(self, idEditorial: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un género con el mismo nombre
            cursor.execute("SELECT idEditorial FROM editorial WHERE idEditorial = %s and statusEditorial = 1", (idEditorial,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A editorial with this Id has already been Activate")

            cursor.execute("UPDATE editorial SET statusEditorial = 1 WHERE idEditorial = %s", (idEditorial,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="Editorial with id %s not found" % idEditorial)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not Active editorial, %s" % str(error))