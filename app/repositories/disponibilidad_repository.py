from ..database.connection import get_db



def establecer_disponibilidad(disponibilidad):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO disponibilidad_medico (rut_medico, inicio_disponibilidad, fin_disponibilidad) VALUES
            (%s, %s, %s)""",
        (disponibilidad.rut_medico, disponibilidad.inicio_disponibilidad, disponibilidad.fin_disponibilidad)
    )
    conn.commit()


def obtener_disponibilidad(rut: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            t.rut,
            t.nombre,
            m.especialidad,
            d.inicio_disponibilidad,
            d.fin_disponibilidad
        FROM 
            trabajador t
        JOIN 
            medico m ON t.rut = m.rut
        JOIN 
            disponibilidad_medico d ON m.rut = d.rut_medico
        WHERE 
            t.rut = %s
        """, (rut,))
    return cursor.fetchall()
