from fastapi import APIRouter, HTTPException, status
from ..models.schemas import Disponibilidad
from ..repositories.disponibilidad_repository import establecer_disponibilidad, obtener_disponibilidad

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def establecer_disponibilidad_endpoint(disponibilidad: Disponibilidad):
    establecer_disponibilidad(disponibilidad)
    return {"Message": "Disponibilidad establecida con éxito"}


@router.get("/{rut}", status_code=status.HTTP_200_OK)
def obtener_horario_medico(rut: str):
    resultado = obtener_disponibilidad(rut)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay disponibilidad con ese rut")
    return {"data": resultado}
