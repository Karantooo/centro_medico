from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import citas, medicos, disponibilidad, usuario
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configuración del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(citas.router, prefix="/Cita", tags=["Citas"])
app.include_router(medicos.router, prefix="/busqueda", tags=["Médicos"])
app.include_router(disponibilidad.router, prefix="/disponibilidad", tags=["Disponibilidad"])
app.include_router(usuario.router, prefix="/usuario", tags=["Usuario"])
