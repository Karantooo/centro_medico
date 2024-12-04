from ..database.connection import get_db
from psycopg2 import OperationalError, DatabaseError
from fastapi import HTTPException
import psycopg2


def obtener_user_rut_paciente(rut: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT contrasenia
            FROM usuario
            JOIN usuario_paciente ON usuario.nombre = usuario_paciente.nombre
            WHERE rut = %s;
    """, (rut,))

    return cursor.fetchone()


def obtener_user_mail_paciente(mail: str):
    conn = get_db()
    cursor = conn.cursor()


def obtener_user_rut_medico(rut: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT u.contrasenia
            FROM usuario u
            JOIN usuario_trabajador up ON u.nombre = up.nombre
            JOIN medico m ON up.rut = m.rut
            WHERE up.rut = %s;
    """, (rut,))

    return cursor.fetchone()


def obtener_user_rut_admin(rut: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.contrasenia
        FROM usuario u
        JOIN usuario_trabajador ut ON u.nombre = ut.nombre
        JOIN administrativo a ON ut.rut = a.rut
        WHERE ut.rut = %s;
    """, (rut,))

    return cursor.fetchone()


def obtener_correo_paciente(rut: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT u.mail as mail_paciente
                   FROM usuario u
                   JOIN usuario_paciente up ON u.nombre = up.nombre
                   WHERE up.rut = '%s'""", (rut))
    
    return cursor.fetchall()