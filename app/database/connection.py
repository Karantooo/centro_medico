import os
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# Variable global para almacenar la conexión
_db_connection = None

def get_db():
    global _db_connection

    # Si la conexión no existe o está cerrada, crear una nueva
    if _db_connection is None or _db_connection.closed != 0:
        while True:
            try:
                _db_connection = psycopg2.connect(
                    host=os.getenv('HOST_DB'),
                    database=os.getenv('DATABASE'),
                    user=os.getenv('USER_DB'),
                    password=os.getenv('PASSWORD_DB'),
                    cursor_factory=RealDictCursor
                )
                print("Database connection was successful")
                break
            except Exception as error:
                print("Database connection failed:", error)
                time.sleep(5)

    return _db_connection
