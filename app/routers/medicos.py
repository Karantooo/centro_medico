from fastapi import APIRouter, HTTPException, status
from ..repositories.medicos_repository import obtener_medicos, obtener_medicos_por_especialidad, obtener_medico_por_rut

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
def mostrar_medicos():
    return {"data": obtener_medicos()}

@router.get("/especialidad/{especialidad}", status_code=status.HTTP_200_OK)
def mostrar_medicos_especialidad(especialidad: str):
    resultado = obtener_medicos_por_especialidad(especialidad)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay médicos disponibles con esta especialidad")
    return {"data": resultado}

@router.get("/rut/{rut}", status_code=status.HTTP_200_OK)
def mostrar_medico(rut: str):
    resultado = obtener_medico_por_rut(rut)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay un médico con ese rut")
    return {"data": resultado}
