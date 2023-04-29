import mysql.connector

class DbConnection:
    def __init__(self, connection=None, success=False, error_message=None):
        self.connection = connection
        self.success = success
        self.error_message = error_message

class DbContext:
    def __init__(self, host=None, user=None, password=None, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            return DbConnection(connection=connection, success=True)
        except mysql.connector.Error as error:
            return DbConnection(success=False, error_message=str(error))
    
    def setDefaultContext(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = 'crud20%'
