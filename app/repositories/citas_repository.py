from ..database.connection import get_db
from psycopg2 import OperationalError, DatabaseError
from fastapi import HTTPException
import psycopg2

def obtener_todas_las_citas():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cita")
    return {"data": cursor.fetchall()}


def obtener_cita_por_id(id: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT c.id_cita, c.rut_doctor, c.rut_paciente, c.estado, c.fecha_inicio, c.fecha_fin, t.nombre 
                   AS nombre_medico, m.especialidad 
                   AS especialidad_medico, p.nombre 
                   AS nombre_paciente 
                   FROM cita c 
                   JOIN medico m ON c.rut_doctor = m.rut 
                   JOIN trabajador t ON m.rut = t.rut 
                   JOIN paciente p ON c.rut_paciente = p.rut	
                   WHERE id_cita = %s""", (id,))
    return cursor.fetchall()


def obtener_mail_paciente(rut: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT mail
        FROM cita
        JOIN paciente ON cita.rut_paciente = paciente.rut
        JOIN usuario_paciente ON usuario_paciente.rut = paciente.rut
        JOIN usuario ON usuario.nombre = usuario_paciente.nombre
        WHERE rut_paciente = %s;
    """,
                   (rut,))
    return cursor.fetchone()



def actualizar_estado_cita(datos):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE cita
            SET estado = %s
            WHERE id_cita = %s""", (datos.estado, datos.id_cita))

        conn.commit()
        return {"Message": "Dato cambiado con éxito"}

    except psycopg2.errors.CheckViolation:
        raise HTTPException(
            status_code=400,
            detail="El estado de la cita no es válido"
        )


def agendar_cita(cita):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """INSERT INTO cita (rut_doctor, rut_paciente, estado, fecha_inicio, fecha_fin) 
            VALUES (%s, %s, %s, %s, %s)""",
            (cita.rut_doctor, cita.rut_paciente, cita.estado, cita.fecha_inicio, cita.fecha_fin))

        conn.commit()
        return {"Message": f"Cita creada correctamente"}

    except (DatabaseError, OperationalError) as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Error en la operación: " + str(e))
