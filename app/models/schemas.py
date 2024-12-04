from pydantic import BaseModel

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


class Usuario(BaseModel):
    rut_paciente: str
    nombre: str
    password: str
    correo: str