from fastapi import APIRouter, HTTPException, status
from ..models.schemas import Usuario
from ..repositories.registro_repository import registrarse

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def registro_usuario(datos: Usuario):
    registrarse(Usuario)
    return {"Message": "Registro exitoso"}

