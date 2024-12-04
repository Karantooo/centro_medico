from ..database.connection import get_db
from psycopg2 import OperationalError, DatabaseError
from fastapi import HTTPException
import psycopg2

def registrarse(Usuario):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO paciente (rut, nombre) 
        VALUES (%s, %s)
        """, Usuario.rut_paciente, Usuario.nombre)
    
        cursor.execute("""
        INSERT INTO usuario (nombre, contrasenia, mail) 
        VALUES (%s, %s, %s)""", Usuario.nombre, Usuario.password, Usuario.correo)
    
        cursor.execute("""
        INSERT INTO usuario_paciente (nombre, rut) 
        VALUES (%s, %s)
        """, Usuario.nombre, Usuario.rut_paciente)

        return {"Message": f"Registro creado con correctamente"}
    


        
    except (DatabaseError, OperationalError) as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Error en la operación: " + str(e))
    

