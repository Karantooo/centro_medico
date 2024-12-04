from ..database.connection import get_db
from psycopg2 import OperationalError, DatabaseError
from fastapi import HTTPException
import psycopg2


def obtener_user_rut_paciente(rut: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT u.nombre, u.mail, u.contrasenia, up.rut
                   FROM usuario u
                   JOIN usuario_paciente up ON u.nombre = up.nombre""")
    
    return cursor.fetchall()


def obtener_user_rut_admin(rut: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT u.nombre, u.mail, u.contrasenia, up.rut
                   FROM usuario u
                   JOIN usuario_trabajador up ON u.nombre = up.nombre""")

    return cursor.fetchall()


def obtener_correo_paciente(rut: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT u.mail as mail_paciente
                   FROM usuario u
                   JOIN usuario_paciente up ON u.nombre = up.nombre
                   WHERE up.rut = '%s'""", (rut))
    
    return cursor.fetchall()