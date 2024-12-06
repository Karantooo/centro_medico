from fastapi import APIRouter, HTTPException, status, BackgroundTasks
from ..models.schemas import Cita, ActualizarEstadoCita
from ..repositories.citas_repository import (obtener_cita_por_id,
                                             actualizar_estado_cita,
                                             agendar_cita,
                                             obtener_todas_las_citas,
                                             obtener_mail_paciente,
                                             obtener_citas_con_rut_paciente,
                                             obtener_citas_con_rut_medico

                                             )
from ..services.cita_service import schedule_email


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def obtenerCitas():
    return obtener_todas_las_citas()


@router.get("/medico/{rut}")
def obtener_citas_rut_medico(rut: str):
    resultado = obtener_citas_con_rut_medico(rut)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")

    return {"data": resultado}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def obtener_cita(id: str):
    resultado = obtener_cita_por_id(id)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
    return {"data": resultado}

@router.patch("/", status_code=status.HTTP_200_OK)
def actualizar_estado_cita_confirmacion(datos: ActualizarEstadoCita):
    actualizar_estado_cita(datos)
    return {"Message": "Dato cambiado con éxito"}

@router.post("/", status_code=status.HTTP_201_CREATED)
def agendar_cita_post(cita: Cita, background_tasks: BackgroundTasks):
    print(cita.rut_doctor)
    agendar_cita(cita)
    #mail = obtener_mail_paciente(cita.rut_paciente)['mail']
    #background_tasks.add_task(schedule_email, cita, mail)
    return {"Message": "Cita creada correctamente"}