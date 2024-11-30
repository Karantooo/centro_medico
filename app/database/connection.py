import os
import psycopg2
from psycopg2.extras import RealDictCursor
import time

def get_db():
    while True:
        try:
            conn = psycopg2.connect(
                host=os.getenv('HOST_DB'),
                database=os.getenv('DATABASE'),
                user=os.getenv('USER_DB'),
                password=os.getenv('PASSWORD_DB'),
                cursor_factory=RealDictCursor
            )
            print("Database connection was successful")
            return conn
        except Exception as error:
            print("Database connection failed:", error)
            time.sleep(5)
