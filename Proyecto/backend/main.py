"""Hello world from the dev team!"""

from typing import Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
from conexion_mongo import agregar_usuario, eliminar_usuario

app = FastAPI(title="ProjecTrack")
app.title = "Seguimiento de proyectos academicos"
app.version = "0.1.0"


# Basic hello world test
@app.get("/Saludo", tags=["Saludo"])
async def hello_root():
    """Just a hello world message. :)"""
    return {"message": "Hello World!", "signs": "The ProjectTrack dev team"}


class Usuario(BaseModel):
    """User scheme with Pydantic validations"""

    cedula: int = Field(
        ..., gt=0, description="Cédula debe ser un número entero positivo."
    )
    nombre: str = Field(
        ..., min_length=3, max_length=50, description="Nombre entre 3 y 50 caracteres."
    )
    email: EmailStr
    edad: int = Field(
        ..., ge=3, description="Edad debe ser un número entero mayor o igual a 3."
    )
    activo: bool
    tipo_de_usuario: Literal["administrador", "profesor", "estudiante"]


@app.post("/usuarios/", tags=["Usuarios"])
def crear_usuario(usuario: Usuario):
    """Add an user to the database"""
    resultado = agregar_usuario(
        cedula=usuario.cedula,
        nombre=usuario.nombre,
        email=usuario.email,
        edad=usuario.edad,
        activo=usuario.activo,
        tipo_de_usuario=usuario.tipo_de_usuario,
    )

    if "error" in resultado:
        raise HTTPException(status_code=400, detail=resultado["error"])

    return resultado


@app.delete("/delete_user/", tags=["Usuarios"])
async def delete_user(cedula: int):
    """Delete an user from the database"""
    resultado = eliminar_usuario(cedula=cedula)

    if "error" in resultado:
        raise HTTPException(status_code=400, detail=resultado["error"])

    return resultado
