from fastapi import APIRouter, HTTPException, status
from ..models.schemas import Cita, ActualizarEstadoCita
from ..repositories.citas_repository import (obtener_cita_por_id,
                                             actualizar_estado_cita,
                                             agendar_cita,
                                             obtener_todas_las_citas)


router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
def obtenerCitas():
    return obtener_todas_las_citas()


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
def agendar_cita_post(cita: Cita):
    print(cita.rut_doctor)
    agendar_cita(cita)
    return {"Message": "Cita creada correctamente"}
