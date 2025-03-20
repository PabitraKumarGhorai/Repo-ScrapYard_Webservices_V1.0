import mysql.connector
import credentials_info
def create_connections():
    connection = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = credentials_info.db_user,
        password = credentials_info.db_password,
        database = credentials_info.mysql_database
    )
    return connection
