from ..database.connection import get_db

def obtener_medicos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT t.rut, t.nombre, m.especialidad FROM trabajador t JOIN medico m ON t.rut = m.rut""")
    return cursor.fetchall()

def obtener_medicos_por_especialidad(especialidad: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT t.rut, t.nombre, m.especialidad FROM trabajador t JOIN medico m ON t.rut = m.rut WHERE m.especialidad = %s""", (especialidad,))
    return cursor.fetchall()

def obtener_medico_por_rut(rut: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT t.rut, t.nombre, m.especialidad FROM trabajador t JOIN medico m ON t.rut = m.rut WHERE t.rut = %s""", (rut,))
    return cursor.fetchall()
