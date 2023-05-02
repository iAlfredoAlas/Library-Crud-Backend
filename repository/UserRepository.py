#Requerid imports
import mysql.connector
from models.user import User
from models.repositoryResponse import RepositoryResponse

##Class of UserRepository
class UserRepository:

    #initialization of the EmployeeUserRepository
    def __init__(self, connection):
        self.connection = connection
    
    #Method getAll User
    def getAll(self, page: int, limit: int):
        offset = (page -1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM user LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        users = [
            {
                "idUser": user[0],
                "nameUser": user[1],
                "carnetUser": user[2],
                "emailUser": user[3],
                "phoneUser": user[4],
                "statusUser": user[5]
            }
            for user in rows
        ]

        return RepositoryResponse(users)
    
    #Method getAllActives
    def getAllActives(self, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE statusUser = 1 LIMIT %s OFFSET %s", (limit, offset))

        rows = cursor.fetchall()
        users = [
            {
                "idUser": user[0],
                "nameUser": user[1],
                "carnetUser": user[2],
                "emailUser": user[3],
                "phoneUser": user[4],
                "statusUser": user[5]
            }
            for user in rows
        ]
        
        return RepositoryResponse(users)
    
    #Method getById Users
    def getById(self, idUser: int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE idUser = %s", (idUser,))
        row = cursor.fetchone()
        if row:
            users = [
            {
                "idUser": row[0],
                "nameUser": row[1],
                "carnetUser": row[2],
                "emailUser": row[3],
                "phoneUser": row[4],
                "statusUser": row[5]
            }
        ]
            return RepositoryResponse(users)
        else:
            return RepositoryResponse(success=False, error_message="User not found")
        
    #Method insert User
    def insert(self, user: User):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE nameUser = %s", (user.nameUser,))

        if cursor.fetchone():
            return RepositoryResponse(success=False, error_message="User already exists")
        else:
            try:
                cursor.execute("INSERT INTO user (nameUser, carnetUser, emailUser, phoneUser) VALUES (%s, %s, %s, %s)", (user.nameUser, user.carnetUser, user.emailUser, user.phoneUser))
                self.connection.commit()
                return RepositoryResponse(success=True)
            except mysql.connector.Error as error:
                return RepositoryResponse(success=False, error_message="Can not insert User, %s" % str(error))
    
    #Method update Users
    def update(self, idUser: int, user: User):
        cursor = self.connection.cursor()
        try:
            # Verificar si existe un User con el mismo nombre
            cursor.execute("SELECT idUser FROM user WHERE nameUser = %s AND idUser != %s", (user.nameUser, idUser))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A user with this name already exists")

            # Actualizar el User
            cursor.execute("UPDATE user SET nameUser = %s, carnetUser = %s, emailUser = %s, phoneUser = %s, statusUser = %s WHERE idUser = %s", (user.nameUser, user.carnetUser, user.emailUser, user.phoneUser, user.statusUser, idUser))
            self.connection.commit()
            if cursor.rowcount == 0:
                return RepositoryResponse(success=False, error_message="User didn't change or user with id %s not found" % user.idUser)
            else:
                return RepositoryResponse(success=True)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not update User, %s" % str(error))
        

    #Method delete User   
    def delete(self, idUser: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un user con ese idUser
            cursor.execute("SELECT idUser FROM user WHERE idUser = %s and statusUser = 0", (idUser,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A user with this Id has already been deleted")

            cursor.execute("UPDATE user SET statusUser = 0 WHERE idUser = %s", (idUser,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="User with id %s not found" % idUser)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not delete User, %s" % str(error))


    #Method activate User
    def activate(self, idUser: int):
        cursor = self.connection.cursor()
        try:
             # Verificar si existe un user con ese idUser
            cursor.execute("SELECT idUser FROM user WHERE idUser = %s and statisUser = 1", (idUser,))
            result = cursor.fetchone()
            if result is not None:
                return RepositoryResponse(success=False, error_message="A user with this Id has already been Activate")

            cursor.execute("UPDATE user SET statusUser = 1 WHERE idUser = %s", (idUser,))
            if cursor.rowcount > 0:
                self.connection.commit()
                return RepositoryResponse(success=True)
            else:
                return RepositoryResponse(success=False, error_message="User with id %s not found" % idUser)
        except mysql.connector.Error as error:
            return RepositoryResponse(success=False, error_message="Can not activate User, %s" % str(error))
