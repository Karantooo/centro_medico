from fastapi import FastAPI
from fastapi.params import Body 
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import OperationalError, DatabaseError
import time

app = FastAPI()

# port = 5432

# Configuración del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Permite el origen de Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

''' 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las fuentes. Cambia esto a ["http://127.0.0.1:5500"] para mayor seguridad.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
'''


class Disponibilidad(BaseModel):
    rut_medico: str
    inicio_disponibilidad: str
    fin_disponibilidad: str

class Cita(BaseModel):
    rut_doctor: str
    rut_paciente: str
    estado: str
    fecha_inicio: str  
    fecha_fin: str    

class ActualizarEstadoCita(BaseModel):
    id_cita: int
    estado: str

while True:
    try:   
        conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password=' ', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful")
        break

    except Exception as error:
        print("Database connection failed")
        time.sleep(5)

#Testeado
# User Story: [US 1] Yo como paciente quiero poder agendar una cita, para ser atendido por un médico.
@app.get("/Cita/{id}", status_code=status.HTTP_200_OK) 
def obtenerCita(id: str):
    cursor.execute("""SELECT c.id_cita, c.rut_doctor, c.rut_paciente, c.estado, c.fecha_inicio, c.fecha_fin, t.nombre 
                   AS nombre_medico, m.especialidad 
                   AS especialidad_medico, p.nombre 
                   AS nombre_paciente 
                   FROM cita c 
                   JOIN medico m ON c.rut_doctor = m.rut 
                   JOIN trabajador t ON m.rut = t.rut 
                   JOIN paciente p ON c.rut_paciente = p.rut	
                   WHERE id_cita = %s""", (id,))

    resultado = cursor.fetchall()

    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
    
    return {"data": resultado}

#Testeado
@app.get("/Cita", status_code=status.HTTP_200_OK)
def obtenerCitas():
    cursor.execute("SELECT * FROM cita")
    return {"data": cursor.fetchall()}

@app.patch("/Cita", status_code=status.HTTP_200_OK)
def actualizarEstadoCita(datos : ActualizarEstadoCita):
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

#Testeado
@app.post("/Cita", status_code=status.HTTP_201_CREATED)
def agendarCitas(cita: Cita):
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
    

# hacer un update de citas
# hacer un get de todas las citas

# User Story: [US 4]Como paciente quiero poder buscar médicos, para ser atendido por un especialista de manera rápida y eficiente.
#Testeado
@app.get("/busqueda", status_code=status.HTTP_200_OK)
def mostrarMedicos():
    cursor.execute("""
        SELECT 
            t.rut,
            t.nombre,
            m.especialidad
        FROM 
            trabajador t
        JOIN 
        medico m ON t.rut = m.rut""")

    
    return {"data": cursor.fetchall()}

#Testeado
@app.get("/busqueda/especialidad/{especialidad}", status_code=status.HTTP_200_OK)
def mostrarMedicosEspecialidad(especialidad: str):
    cursor.execute("""
        SELECT 
            t.rut,
            t.nombre,
            m.especialidad
        FROM 
            trabajador t
        JOIN 
            medico m ON t.rut = m.rut
        WHERE 
            m.especialidad = %s""", (especialidad,))
    resultado = cursor.fetchall()

    if not resultado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay medicos disponibles con esta especialidad"
        )
    return {"data": resultado}

#Testeado
@app.get("/busqueda/rut/{rut}", status_code=status.HTTP_200_OK) # {id}: path parameter
def mostrarMedico(rut: str):
    #if id != 1:
    #    raise HTTPException(status_code=404, detail="Error 404: Médico no encontrado")
    cursor.execute("""
        SELECT 
            t.rut,
            t.nombre,
            m.especialidad
        FROM 
            trabajador t
        JOIN 
            medico m ON t.rut = m.rut
        WHERE 
            t.rut = %s""", (rut,))
    resultado = cursor.fetchall()

    if not resultado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay un medico con ese rut"
        )
    return {"data": resultado}


#User Story: [US 5] Como médico quiero poder establecer mi disponibilidad, para poder mostrar a los pacientes horas disponibles.
#Testeado
@app.post("/disponibilidad", status_code=status.HTTP_201_CREATED)
def establecerDisponibilidad(disponibilidad: Disponibilidad):
    cursor.execute(
        """INSERT INTO disponibilidad_medico (rut_medico, inicio_disponibilidad, fin_disponibilidad) VALUES
            (%s, %s, %s)""", 
        (disponibilidad.rut_medico, disponibilidad.inicio_disponibilidad, disponibilidad.fin_disponibilidad))
    
    conn.commit()
    return{"Message": "Disponibilidad establecida con éxito"}

#Testeado a
@app.get("/disponibilidad/{rut}", status_code=status.HTTP_200_OK) # id del médico (supongo que el rut)
def obtenerHorarioMedico(rut: str):
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
            t.rut = %s""", (rut,))

    resultado = cursor.fetchall()

    if not resultado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay disponibilidad con ese rut"
        )
    return {"data": resultado}

    

#User Story: [US 9  ] Como paciente quiero recibir notificaciones de citas agendadas, para evitar asi mi ausencia.
@app.get("/notificaciones", status_code=status.HTTP_200_OK)
def notificaciones():
    return {"data": "Notificaciones de usuarios"}


# Login
@app.post("/Login", status_code=status.HTTP_201_CREATED)
def login():
    return {"Message": "Usuario logeado con éxito"}


















