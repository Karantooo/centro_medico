from fastapi import APIRouter, HTTPException, status
from ..repositories.usuario_repository import (obtener_user_rut_admin,
                                                obtener_user_rut_paciente, obtener_correo_paciente)
from ..models.schemas import Login

router = APIRouter()


@router.get("/paciente/{rut}", status_code=status.HTTP_200_OK)
def obtener_usuario_rut_paciente(rut: str):
    resultado = obtener_user_rut_paciente(rut)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
    return {"data": resultado}


# @router.post("/paciente_login", status_code=status.HTTP_200_OK)
# def obtener_usuario_rut_paciente(login: Login):
#     if
#
#
#     if not resultado:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
#     return {"data": resultado}


@router.get("/admin/{rut}", status_code=status.HTTP_200_OK)
def obtener_usuario_rut_medico(rut: str):
    resultado = obtener_user_rut_admin(rut)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
    return {"data": resultado}


@router.get("/correo/{rut}", status_code=status.HTTP_200_OK)
def obtener_correo_paciente(rut: str):
    resultado = obtener_correo_paciente(rut)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
    return {"data": resultado}